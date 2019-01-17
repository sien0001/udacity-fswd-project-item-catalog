import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY") or "default secret key"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") or \
        "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATION = False


class GoogleAuthConfig(object):
    CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID") or "default client id"
    CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET") or \
        "default client secret"
