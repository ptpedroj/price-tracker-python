from bs4 import BeautifulSoup
from src.common.database import Database
from src.models.items.constants import ItemConstants
from src.models.stores.store import Store
import re
import requests
import uuid


class Item(object):
    def __init__(self, name: str, url: str, store_id: str, _id: str = None) -> None:
        self.name = name
        self.store = Store.get_by_id(store_id)
        self.url = url
        self.__price = None
        self._id = uuid.uuid4().hex if _id == None else _id


    def __repr__(self):
        return f"Item('{self.name}', '{self.url}', '{self.store._id}', '{self._id}')"


    def __str__(self):
        return f"<Item {self.name} with ID {self._id} at price {self.price} with URL {self.url} at store {self.store.name} with ID {self.store._id}>"


    @property
    def price(self):
        if self.__price == None:
            self.__price = self.__load_price__(self.store.tag_name, self.store.query)
        return self.__price


    def __load_price__(self, tag_name, query):
        # Amazon: <span id="priceblock_ourprice" class="a-size-medium a-color-price">$31.00</span>
        request = requests.get(self.url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(tag_name, query)
        string_price = element.text.strip()
        pattern = re.compile("\d+\.\d+")
        match = pattern.search(string_price)
        return float(match.group())


    def update_price(self):
        self.__price = None
        return self.price


    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "url": self.url,
            "store_id": self.store._id
        }


    def save_to_db(self):
        Database.insert(ItemConstants.COLLECTION, self.json())


    @classmethod
    def get_by_id(cls, _id):
        return Item(**Database.find_one(ItemConstants.COLLECTION, {"_id": _id}))