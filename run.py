from app import app, db

import os

# Initialize the database on startup (via 'flask run' command)
db.create_all()

# OAuth 2.0 works over SSL layer. In the development environment
# (non production) we disable/relax this restriction.
# REMOVE IF RUNNING IN PRODUCTION.
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

if __name__ == "__main__":
    db.create_all()
    app.run()
