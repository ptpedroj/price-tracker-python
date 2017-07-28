from flask import Flask
from src.common.database import Database

app = Flask(__name__)
app.config.from_object("src.config")
app.secret_key = "123"

@app.before_first_request
def init():
    Database.initialize()


@app.route("/")
def default():
    pass


from src.models.users.views import user_blueprint
app.register_blueprint(user_blueprint, url_prefix = "/users")