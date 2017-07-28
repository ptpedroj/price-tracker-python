from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

DEBUG = True
ADMINS = frozenset([
    "ptpedroj@gmail.com"
])

MAIL_API_URL = os.environ.get("MAIL_API_URL")
MAIL_API_KEY = os.environ.get("MAIL_API_KEY")
MAIL_FROM = os.environ.get("MAIL_FROM")
PRICE_TRACKER_DB_NAME = os.environ.get("PRICE_TRACKER_DB_NAME")
PRICE_TRACKER_DB_URI = os.environ.get("PRICE_TRACKER_DB_URI")