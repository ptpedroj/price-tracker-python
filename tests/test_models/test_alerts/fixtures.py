from src.models.alerts.alert import Alert
from tests.test_models.test_users.test_user import user
from tests.test_models.test_items.test_item import item
from datetime import datetime
from unittest import mock
import pytest


@pytest.fixture
def price_limit():
    return 10.00


@pytest.fixture
def last_checked():
    return datetime(2007, 12, 6, 16, 29, 43, 79043)


@pytest.fixture
def alert_id():
    return "cde345"

@pytest.fixture
@mock.patch("src.models.users.user.User.get_by_id")
@mock.patch("src.models.items.item.Item.get_by_id")
def alert(mock_item_get_by_id, mock_user_get_by_id, user, item, price_limit, last_checked, alert_id):
    mock_user_get_by_id.return_value = user
    mock_item_get_by_id.return_value = item
    return Alert(user._id, price_limit, item._id, last_checked, alert_id)








