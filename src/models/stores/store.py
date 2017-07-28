from src.common.database import Database
from src.models.stores.constants import StoreConstants
import uuid

class Store(object):
    def __init__(self, name: str, base_url: str, tag_name: str, query: str, _id: uuid = None) -> None:
        self.name = name
        self.base_url = base_url
        self.tag_name = tag_name
        self.query = query
        self._id = uuid.uuid4().hex if _id == None else _id


    def __repr__(self):
        return f"Store('{self.name}', '{self.base_url}', '{self.tag_name}', {self.query}, '{self._id}')"


    def __str__(self):
        return f"<Store {self.name} with ID {self._id} at URL {self.base_url} - tag name {self.tag_name} - query {self.query}>"


    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "base_url": self.base_url,
            "tag_name": self.tag_name,
            "query": self.query
        }



    def save_to_db(self):
        Database.insert(StoreConstants.COLLECTION, self.json())


    @classmethod
    def get_by_id(cls, _id):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"_id": _id}))


    @classmethod
    def get_by_name(cls, name):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"name": name}))


    @classmethod
    def get_by_partial_url(cls, partial_url):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"base_url": {"$regex": f"^{partial_url}"}}))


    @classmethod
    def get_by_url(cls, url):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"base_url": url}))
