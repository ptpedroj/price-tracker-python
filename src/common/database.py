import pymongo as pm

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DB = None


    @classmethod
    def initialize(cls, db_name = "price_tracker"):
        client = pm.MongoClient(Database.URI)
        cls.DB = client[db_name]


    @classmethod
    def insert(cls, collection, data, key = None):
        if cls.DB is None:
            cls.initialize()
        if key == None:
            return cls.DB[collection].insert_one(data)
        else:
            return cls.DB[collection].replace_one(key, data, True)


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