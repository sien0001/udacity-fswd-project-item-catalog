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


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, index=True)

    items = db.relationship("Item", backref="item", lazy=True)


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey(Category.id),
        nullable=False
    )
    title = db.Column(db.String(100), unique=True, index=True)
    description = db.Column(db.String(250))

    category = db.relationship(Category)
