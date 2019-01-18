from app import db

from flask_login import UserMixin
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    name = db.Column(db.String(250))


class OAuth(db.Model, OAuthConsumerMixin):
    __tablename__ = "oauth"

    provider_user_id = db.Column(db.String(250), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    user = db.relationship(User)
