import src.models.stores.views as views


class TestViews(object):
    def test_var_store_blueprint(self):
        assert hasattr(views, "store_blueprint")


    def test_store(self):
        pass