from src.common.database import Database
from tests.test_common.fixtures import collection, data, query
from unittest import mock
import pymongo

class TestDatabase(object):
    def test_db(self):
        assert hasattr(Database, "DB")


    @mock.patch("pymongo.MongoClient")
    def test_initialize(self, mock_pymongo):
        Database.initialize()
        assert mock_pymongo.called


    @mock.patch("src.common.database.Database.DB")
    def test_insert_no_key(self, mock_db, collection, data):
        mock_db_insert = mock.MagicMock()
        mock_db.__getitem__.return_value = mock_db_insert
        Database.insert(collection, data)
        assert mock_db_insert.insert_one.call_count == 1 # mock_db_insert.insert_one.called was always returning True.


    @mock.patch("src.common.database.Database.DB")
    def test_insert_with_key(self, mock_db, collection, data, query):
        mock_db_update = mock.Mock()
        mock_db.__getitem__.return_value = mock_db_update
        Database.insert(collection, data, query)
        assert mock_db_update.replace_one.call_count == 1 #mock_db_update.replace_one.called was always returning True.


    @mock.patch("src.common.database.Database.DB")
    def test_find(self, mock_db, collection, query):
        mock_db_find = mock.Mock()
        mock_db.__getitem__.return_value = mock_db_find
        Database.find(collection, query)
        assert mock_db_find.find.call_count == 1 # mock_db_find.find.called was always returning True.


    @mock.patch("src.common.database.Database.DB")
    def test_find_one(self, mock_db, collection, query):
        mock_db_find_one = mock.Mock()
        mock_db.__getitem__.return_value = mock_db_find_one
        Database.find_one(collection, query)
        assert mock_db_find_one.find_one.call_count == 1 #mock_db_find_one.find_one.called was always returning True.