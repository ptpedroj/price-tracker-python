from src.models.items.constants import ItemConstants
from src.models.items.item import Item
from tests.test_models.test_items.fixtures import name, url, item_id, price, item, content, request
from tests.test_models.test_stores.fixtures import store_id, store, base_url, tag_name, query
from unittest import mock


class TestItem(object):
    @mock.patch("src.models.stores.store.Store.get_by_id")
    def test_create_item(self, mock_store_get_by_id, store, name, url, store_id, item_id) -> Item:
        mock_store_get_by_id.return_value = store
        test_item = Item(name, url, store_id, item_id)
        assert test_item.name == name and \
            test_item.url == url and \
            test_item.store._id == store_id and \
            test_item._id == item_id

    @mock.patch("src.models.stores.store.Store.get_by_id")
    def test_item_repr(self, mock_store_get_by_id, store, item, name, price, url):
        mock_store_get_by_id.return_value = store
        assert repr(item) == repr(eval(repr(item)))


    @mock.patch("src.models.items.item.Item.price")
    def test_item_str(self, mock_item_price, price, item):
        mock_item_price.return_value = price
        assert str(item).startswith("<Item")


    @mock.patch("src.models.items.item.Item.__load_price__")
    def test_item_price(self, mock_item_load_price, price, item):
        mock_item_load_price.return_value = price
        assert item.price == price


    @mock.patch("requests.get")
    def test_item_load_price(self, mock_request_get, request, item, price):
        mock_request_get.return_value = request
        assert item.price == price


    @mock.patch("src.models.items.item.Item.__load_price__")
    def test_item_update_price(self, mock_item_load_price, price, item):
        mock_item_load_price.return_value = price
        assert item.update_price() == price


    def test_json(self, item):
        item_json = item.json()
        assert item_json["_id"] == item._id and \
            item_json["name"] == item.name and \
            item_json["url"] == item.url and \
            item_json["store_id"] == item.store._id


    @mock.patch("src.common.database.Database.insert")
    def test_save_to_db(self, mock_insert, item):
        item.save_to_db()
        assert mock_insert.called_with(ItemConstants.COLLECTION, item.json())


    @mock.patch("src.common.database.Database.find_one")
    @mock.patch("src.models.stores.store.Store.get_by_id")
    def test_get_by_id(self, mock_store_get_by_id, mock_find_one, store, item_id, item):
        mock_store_get_by_id.return_value = store
        mock_find_one.return_value = item.json()
        result = Item.get_by_id(item_id)
        assert repr(result) == repr(item) and \
            mock_find_one.called_with(ItemConstants.COLLECTION, {"_id": item_id})