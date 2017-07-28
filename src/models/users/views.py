from flask import Blueprint, redirect, request, session, url_for, render_template
from src.models.users.user import User

import src.models.users.errors as UserErrors


user_blueprint = Blueprint('users', __name__)


@user_blueprint.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            if User.is_login_valid(email, password):
                session["email"] = email
                return redirect(url_for(".alerts"))

        except UserErrors.UserError as err:
            return err.message


    return render_template("users/login.html")



@user_blueprint.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            if User.register_user(email, password):
                session["email"] = email
                return redirect(url_for(".alerts"))

        except UserErrors.UserError as err:
            return err.message


    return render_template("users/register.html")


@user_blueprint.route("/alerts")
def alerts():
    return ""


@user_blueprint.route("/logout")
def logout():
    pass


@user_blueprint.route("/check_alerts/<string:user_id>")
def check_user_alerts(user_id):
    pass