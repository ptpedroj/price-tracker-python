from src.models.stores.store import Store
import pytest


@pytest.fixture
def name():
    return "test_store"


@pytest.fixture
def base_url():
    return "https://test.com/"


@pytest.fixture
def tag_name():
    return "span"


@pytest.fixture
def query():
    return {"id": "priceblock_ourprice"}


@pytest.fixture
def store_id():
    return "123abc"


@pytest.fixture
def store(name, base_url, tag_name, query, store_id):
    return Store(name, base_url, tag_name, query, store_id)