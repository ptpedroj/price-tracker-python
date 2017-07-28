import src.settings as settings

class AlertConstants(object):
    COLLECTION = "alerts"

    MAIL_API_URL = settings.MAIL_API_URL
    MAIL_API_KEY = settings.MAIL_API_KEY
    MAIL_FROM = settings.MAIL_FROM

    ALERT_AGE_MINUTES = 10