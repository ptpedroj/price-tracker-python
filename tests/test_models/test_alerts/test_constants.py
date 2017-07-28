from src.models.alerts.constants import AlertConstants

class TestConstants(object):
    def test_has_collection_constant(self):
        assert hasattr(AlertConstants, "COLLECTION")


    def test_has_mail_api_url_constant(self):
        assert hasattr(AlertConstants, "MAIL_API_URL")


    def test_has_mail_api_key_constant(self):
        assert hasattr(AlertConstants, "MAIL_API_KEY")


    def test_has_mail_from_constant(self):
        assert hasattr(AlertConstants, "MAIL_FROM")


    def test_has_alert_age_minutes(self):
        assert hasattr(AlertConstants, "ALERT_AGE_MINUTES")