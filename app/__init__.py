from config import Config, GoogleAuthConfig

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_dance.contrib.google import make_google_blueprint
from flask_dance.consumer.backend.sqla import SQLAlchemyBackend
from flask_login import current_user, LoginManager
from flask_restful import Api

# Initialize the Flask app, load in the Config via object
# and attach the Bootstrap extension
app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

# Configure the database (SQLAlchemy)
db = SQLAlchemy(app)
from app import models

# Configure the API endpoints (Flask-Restful)
from app.api import Catalog
api = Api(app)
api.add_resource(Catalog, "/api/catalog")

# Configure Google OAuth dance and blueprint
blueprint = make_google_blueprint(
    client_id=GoogleAuthConfig.CLIENT_ID,
    client_secret=GoogleAuthConfig.CLIENT_SECRET,
    scope=["email", "profile"]
)
app.register_blueprint(blueprint, url_prefix="/login")
blueprint.backend = SQLAlchemyBackend(
    model=models.OAuth,
    session=db.session,
    user=current_user
)
from app.utils import google_logged_in

# Setup the login manager
login_manager = LoginManager()
login_manager.login_view = "google.login"
login_manager.init_app(app)


# Util function used by login_manager to retrieve
# the user object from the database.
@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))


# Configure the routes
from app import views
