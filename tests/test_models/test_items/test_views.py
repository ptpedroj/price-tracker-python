import src.models.items.views as views


class TestViews(object):
    def test_var_item_blueprint(self):
        assert hasattr(views, "item_blueprint")


    def test_item(self):
        pass