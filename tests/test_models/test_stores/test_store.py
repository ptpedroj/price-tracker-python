from src.models.stores.constants import StoreConstants
from src.models.stores.store import Store
from tests.test_models.test_stores.fixtures import name, base_url, tag_name, query, store_id, store
from unittest import mock


class TestStore(object):
    def test_create_store(self, name, base_url, tag_name, query, store_id):
        test_store = Store(name, base_url, tag_name, query, store_id)
        assert test_store.name == name and \
            test_store.base_url == base_url and \
            test_store.tag_name == tag_name and \
            test_store.query == query and \
            test_store._id == store_id


    def test_repr(self, store):
        assert repr(store) == repr(eval(repr(store)))


    def test_str(self, store):
        assert str(store).startswith("<Store")


    def test_json(self, store):
        store_json = store.json()
        assert store_json["_id"] == store._id and \
            store_json["base_url"] == store.base_url and \
            store_json["tag_name"] == store.tag_name and \
            store_json["query"] == store.query


    @mock.patch("src.common.database.Database.insert")
    def test_save_to_db(self, mock_insert, store):
        store.save_to_db()
        assert mock_insert.called_with(StoreConstants.COLLECTION, store.json())


    @mock.patch("src.common.database.Database.find_one")
    def test_get_by_id(self, mock_find_one, store_id, store):
        mock_find_one.return_value = store.__dict__
        result = Store.get_by_id(store_id)
        assert repr(result) == repr(store) and \
            mock_find_one.called_with(StoreConstants.COLLECTION, {"_id": store_id})


    @mock.patch("src.common.database.Database.find_one")
    def test_get_by_name(self, mock_find_one, name, store):
        mock_find_one.return_value = store.__dict__
        result = Store.get_by_name(name)
        assert repr(result) == repr(store) and \
            mock_find_one.called_with(StoreConstants.COLLECTION, {"name": name})


    @mock.patch("src.common.database.Database.find_one")
    def test_get_by_partial_url(self, mock_find_one, base_url, store):
        mock_find_one.return_value = store.__dict__
        partial_url = base_url[:(len(base_url) // 2)]
        result = Store.get_by_partial_url(partial_url)
        assert repr(result) == repr(store) and \
            mock_find_one.called_with(StoreConstants.COLLECTION, {"base_url": {"$regex": f"^{partial_url}"}})


    @mock.patch("src.common.database.Database.find_one")
    def test_get_by_url(self, mock_find_one, base_url, store):
        mock_find_one.return_value = store.__dict__
        result = Store.get_by_url(base_url)
        assert repr(result) == repr(store) and \
            mock_find_one.called_with(StoreConstants.COLLECTION, {"base_url": base_url})