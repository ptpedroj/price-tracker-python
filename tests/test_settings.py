import src.settings as settings

class TestConfig(object):
    def test_debug(self):
        assert hasattr(settings, "DEBUG")


    def test_admins(self):
        assert isinstance(settings.ADMINS, frozenset)


    def test_has_mail_api_url_constant(self):
        assert hasattr(settings, "MAIL_API_URL")


    def test_has_mail_api_key_constant(self):
        assert hasattr(settings, "MAIL_API_KEY")


    def test_has_mail_from_constant(self):
        assert hasattr(settings, "MAIL_FROM")