from src.models.items.item import Item
from src.models.users.user import User
from src.models.alerts.constants import AlertConstants
from src.common.database import Database
from datetime import datetime, timedelta

import requests
import uuid

class Alert(object):
    def __init__(self, user_id: str, price_limit: float, item_id: str, last_checked: datetime = None, _id: str = None) -> None:
        self.user = User.get_by_id(user_id)
        self.price_limit = price_limit
        self.item = Item.get_by_id(item_id)
        self._id = uuid.uuid4().hex if _id == None else _id
        self.last_checked = datetime.utcnow() if last_checked == None else last_checked


    def __repr__(self):
        last_checked = None if self.last_checked == None else f"'{self.last_checked}'"
        _id = None if self._id == None else f"'{self._id}'"
        return f"Alert('{self.user._id}', {self.price_limit}, '{self.item._id}', {last_checked}, {_id})"


    def __str__(self):
        return f"<Alert ID {self._id} last checked {self.last_checked} for {self.user.email} with ID {self.user._id} on item {self.item.name} with ID {self.item._id} with price limit {self.price_limit}>"


    def send(self):
        return requests.post(
            AlertConstants.MAIL_API_URL,
            auth=("api", AlertConstants.MAIL_API_KEY),
            data={"from": AlertConstants.MAIL_FROM,
                  "to": self.user.email,
                  "subject": f"Price Alert for {self.item.name}",
                  "text": str(self)})


    def json(self):
        return {
            "_id": self._id,
            "user_id": self.user._id,
            "price_limit": self.price_limit,
            "item_id": self.item._id,
            "last_checked": self.last_checked
        }


    def save_to_db(self):
        Database.insert(AlertConstants.COLLECTION, self.json(), {"_id": self._id})


    @classmethod
    def get_by_id(cls, _id):
        return Alert(**Database.find_one(AlertConstants.COLLECTION, {"_id": _id}))


    @classmethod
    def get_alerts_to_update(cls, age_minutes = AlertConstants.ALERT_AGE_MINUTES):
        last_checked_limit = datetime.utcnow() - timedelta(minutes = age_minutes)
        return [cls(**alert) for alert in Database.find(AlertConstants.COLLECTION,
                                                        {"last_checked":
                                                             {"$lte": last_checked_limit}
                                                        }
                                                       )]


    def update(self):
        price = self.item.update_price()
        self.last_checked = datetime.utcnow()
        self.save_to_db()
        return price


    def check_price_limit_reached(self):
        if self.item.price <= self.price_limit:
            return self.send()