from src.settings import PRICE_TRACKER_DB_NAME, PRICE_TRACKER_DB_URI
import pymongo as pm

class Database(object):
    DB = None


    @classmethod
    def initialize(cls, db_uri = PRICE_TRACKER_DB_URI, db_name = PRICE_TRACKER_DB_NAME):
        client = pm.MongoClient(db_uri)
        cls.DB = client[db_name]


    @classmethod
    def insert(cls, collection, data, query = None):
        if cls.DB is None:
            cls.initialize()
        if query == None:
            return cls.DB[collection].insert_one(data)
        else:
            return cls.DB[collection].replace_one(query, data, True)


    @classmethod
    def find(cls, collection, query):
        if cls.DB is None:
            cls.initialize()
        return cls.DB[collection].find(query)


    @classmethod
    def find_one(cls, collection, query):
        if cls.DB is None:
            cls.initialize()
        return cls.DB[collection].find_one(query)