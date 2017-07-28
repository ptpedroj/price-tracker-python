from flask import Blueprint

import pytest
import src.models.alerts.views as views


class TestViews(object):
    def test_var_alert_blueprint(self):
        assert hasattr(views, "alert_blueprint") and \
            isinstance(views.alert_blueprint, Blueprint) and \
            views.alert_blueprint.name == "alerts"


    def test_create_alert(self):
        pass


    def test_deactivate_alert(self):
        pass


    def test_get_alert_page(self):
        pass


    def test_get_alerts_for_user(user_id):
        pass