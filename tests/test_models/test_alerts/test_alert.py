from src.models.alerts.alert import Alert
from src.models.alerts.constants import AlertConstants
from tests.test_models.test_users.fixtures import user, email, password, user_id
from tests.test_models.test_stores.fixtures import store, store_id, tag_name, query, base_url, name
from tests.test_models.test_items.fixtures import item, url, item_id
from tests.test_models.test_alerts.fixtures import alert, price_limit, last_checked, alert_id
from unittest import mock
import pytest


class TestAlert(object):
    @mock.patch("src.models.users.user.User.get_by_id")
    @mock.patch("src.models.items.item.Item.get_by_id")
    def test_create_alert_no_last_checked(self, mock_item_get_by_id, mock_user_get_by_id, user, price_limit, item):
        mock_user_get_by_id.return_value = user
        mock_item_get_by_id.return_value = item
        test_alert = Alert(user._id, price_limit, item._id)
        assert test_alert.user is user and \
            test_alert.price_limit == price_limit and \
            test_alert.item is item


    @mock.patch("src.models.users.user.User.get_by_id")
    @mock.patch("src.models.items.item.Item.get_by_id")
    def test_create_alert_with_last_checked(self, mock_item_get_by_id, mock_user_get_by_id, user, price_limit, item, last_checked):
        mock_user_get_by_id.return_value = user
        mock_item_get_by_id.return_value = item
        test_alert = Alert(user._id, price_limit, item._id, last_checked)
        assert test_alert.user is user and \
            test_alert.price_limit == price_limit and \
            test_alert.item is item and \
            test_alert.last_checked is last_checked


    @mock.patch("src.models.users.user.User.get_by_id")
    @mock.patch("src.models.items.item.Item.get_by_id")
    def test_alert_repr(self, mock_item_get_by_id, mock_user_get_by_id, alert, user, price_limit, item):
        mock_user_get_by_id.return_value = user
        mock_item_get_by_id.return_value = item
        assert repr(alert) == repr(eval(repr(alert)))


    def test_alert_str(self, alert, user, price_limit, item):
        assert str(alert).startswith("<Alert")


    @mock.patch("requests.post")
    def test_send(self, mock_request_post, alert):
        alert.send()
        assert mock_request_post.called


    def test_json(self, alert):
        alert_json = alert.json()
        assert alert_json["_id"] == alert._id and \
            alert_json["user_id"] == alert.user._id and \
            alert_json["price_limit"] == alert.price_limit and \
            alert_json["item_id"] == alert.item._id and \
            alert_json["last_checked"] == alert.last_checked


    @mock.patch("src.common.database.Database.insert")
    def test_save_to_db(self, mock_insert, alert):
        alert.save_to_db()
        assert mock_insert.called_with(AlertConstants.COLLECTION, alert.json())


    @mock.patch("src.common.database.Database.find_one")
    @mock.patch("src.models.users.user.User.get_by_id")
    @mock.patch("src.models.items.item.Item.get_by_id")
    def test_get_by_id(self, mock_item_get_by_id, mock_user_get_by_id, mock_find_one, item, user, alert_id, alert):
        mock_item_get_by_id.return_value = item
        mock_user_get_by_id.return_value = user
        mock_find_one.return_value = alert.json()
        result = Alert.get_by_id(alert_id)
        assert repr(result) == repr(alert) and \
            mock_find_one.called_with(AlertConstants.COLLECTION, {"_id": alert_id})


    @mock.patch("src.common.database.Database.find")
    @mock.patch("src.models.users.user.User.get_by_id")
    @mock.patch("src.models.items.item.Item.get_by_id")
    def test_get_alert_to_update(self, mock_item_get_by_id, mock_user_get_by_id, mock_db_find, alert, item, user):
        mock_db_find.return_value = [alert.json()]
        mock_item_get_by_id.return_value = item
        mock_user_get_by_id.return_value = user
        test_result = Alert.get_alerts_to_update(1)
        assert repr(test_result[0]) == repr(alert) and \
            mock_db_find.called



    @mock.patch("src.models.alerts.alert.Alert.save_to_db")
    @mock.patch("src.models.items.item.Item.update_price")
    def test_update(self, mock_item_update_price, mock_alert_save_to_db, alert, price_limit):
        mock_item_update_price.return_value = price_limit - 1.0
        test_price = alert.update()
        assert test_price == price_limit - 1.0 and \
            mock_item_update_price.called and \
            mock_alert_save_to_db.called


    CHECK_PRICE_LIMIT_PARAMS = [
        (price_limit() - 1.0, True),
        (price_limit() + 1.0, False)
    ]
    @mock.patch("src.models.alerts.alert.Alert.send")
    @mock.patch("src.models.items.item.Item.price", new_callable = mock.PropertyMock)
    @pytest.mark.parametrize("test_price, is_under_price_limit", CHECK_PRICE_LIMIT_PARAMS)
    def test_check_price_limit_reached(self, mock_item_price, mock_alert_send, alert, price_limit, test_price, is_under_price_limit):
        mock_item_price.return_value = test_price
        alert.check_price_limit_reached()
        assert mock_alert_send.called == is_under_price_limit
