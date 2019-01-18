from config import Config, GoogleAuthConfig

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app, load in the Config via object
# and attach the Bootstrap extension
app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

# Configure the database (SQLAlchemy)
db = SQLAlchemy(app)
from app import models

# Configure the routes
from app import views
