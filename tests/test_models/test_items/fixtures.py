from src.models.items.item import Item
from unittest import mock
from tests.test_models.test_stores.fixtures import store, store_id
import pytest



@pytest.fixture
def name() -> str:
    return "test_item"


@pytest.fixture
def url(name) -> str:
    return "https://test.com/" + name


@pytest.fixture
def item_id() -> str:
    return "bcd234"


@pytest.fixture
def price() -> float:
    return 123.45


@pytest.fixture
@mock.patch("src.models.stores.store.Store.get_by_id")
def item(mock_store_get_by_id, store, name, url, store_id, item_id) -> Item:
    mock_store_get_by_id.return_value = store
    return Item(name, url, store_id, item_id)


@pytest.fixture
def content(price) -> str:
    return f'<span id="priceblock_ourprice" class="a-size-medium a-color-price">{price}</span>'



class Request(object):
    def __init__(self, content):
        self.__content = content

    @property
    def content(self):
        return self.__content



@pytest.fixture
def request(content):
    return Request(content)