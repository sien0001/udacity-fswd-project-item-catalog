from app import blueprint, db
from app.models import User, OAuth

from flask_dance.consumer import oauth_authorized, oauth_error
from flask_dance.contrib.google import google
from flask_login import login_user
from sqlalchemy.orm.exc import NoResultFound


# Util function which will manage the registration of
# the account with the local db instance upon successful
# OAuth authentication with Google.
@oauth_authorized.connect_via(blueprint)
def google_logged_in(blueprint, token):
    if not token:
        flash("Failed to login with Google credentials.", category="danger")
        return False

    resp = google.get("oauth2/v2/userinfo")
    if not resp.ok:
        flash("Failed to fetch user info from Google.", category="danger")
        return False

    google_info = resp.json()
    google_user_id = google_info.get("id")

    # Check the database for existing OAuth token; if one isnt'
    # there create one.
    try:
        oauth = OAuth.query.filter_by(
            provider=blueprint.name,
            provider_user_id=google_user_id
        ).one()
    except NoResultFound:
        oauth = User(
            provider=blueprint.name,
            provider_user_id=google_user_id,
            token=token
        )

    if oauth.user:
        login_user(oauth.user)
        flash(f"{oauth.user.name}, login successful.", category="primary")
    else:
        user = User(
            email=google_info("email"),
            name=google_info("name")
        )
        oauth.user = user
        db.session.add_all([user, oauth])
        db.session.commit()
        login_user(user)
        flash(f"{user.name}, registration successful.", category="primary")

    # Short-circuit Flask-Dance'es default behaviour
    return False
