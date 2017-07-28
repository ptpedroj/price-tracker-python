import src.config as config

class TestConfig(object):
    def test_debug(self):
        assert hasattr(config, "DEBUG")


    def test_admins(self):
        assert isinstance(config.ADMINS, frozenset)