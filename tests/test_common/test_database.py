from src.common.database import Database

import pymongo

class TestDatabase(object):
    def test_uri(self):
        assert hasattr(Database, "URI")
        assert Database.URI == "mongodb://127.0.0.1:27017"


    def test_db(self):
        assert hasattr(Database, "DB")


    def test_initialize(self):
        Database.initialize()
        assert Database.DB is not None and \
            isinstance(Database.DB, pymongo.database.Database)


    def test_insert(self):
        pass


    def test_find(self):
        pass


    def test_find_one(self):
        pass