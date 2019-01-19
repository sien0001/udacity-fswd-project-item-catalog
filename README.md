# Catalog App

This Catalog App was build as a project submission for the Full Stack Web Developer Udacity Nanodegree.


## Getting Started

Please follow these instructions to get a copy of this project up and running on your local machine.  

### Prerequisites

The Catalog App uses OAuth 2.0 authorization to access Google APIs. You will require valid authorization credentials to connect this application to Google's OAuth2 server. Please follow the instruction from Goolge on how to properly configure [OAuth 2.0 for Client-side Web Applications](https://developers.google.com/identity/protocols/OAuth2UserAgent).

Specify the following Authorised redirect URIs in your OAuth Client credentials configuration.

```
http://127.0.0.1:5000/login/google/authorized
http://localhost:5000/login/google/authorized
```

Once you have obtained Google OAuth credentials, set these as Environmental Variables in your shell.

```
export GOOGLE_CLIENT_ID="<paste your Client ID key here>"
export GOOGLE_CLIENT_SECRET="<paste your Client secret key here>"
```

### Installing

Please follow these step by step instructions to help you get the application running on your local MacOS or Linux machine. 

Initialize the Python virtual environment.

```
python3.7 -m venv catalog-app
source catalog-app/bin/activate
```

Initialize the Google OAuth credentials in evnironment variables (within the virtualenv).

```
export GOOGLE_CLIENT_ID="<paste your Client ID key here>"
export GOOGLE_CLIENT_SECRET="<paste your Client secret key here>"
```

Clone the code repository, and install the required Python packages.

```
cd catalog-app; git clone git@github.com:greg-marcin-sienkiewicz/udacity-fswd-project-item-catalog.git
cd udacity-fswd-project-item-catalog
pip install -r requirements.txt
```

Set the __FLASK_APP__ environment variable to instruct which module __flask run__ to load.

```
export FLASK_APP="run.py"
flask run
```

The application web server should now be running at (http://127.0.0.1:5000/)

## Built With

* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - ORM
* [Flask-Dance](https://flask-dance.readthedocs.io/en/latest/) - OAuth Library
* [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/) - Library for Bootstrap helpers
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/) - Session management
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) - Extension for building REST APIs
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) - WTForms integration

## Authors

* **Greg Sienkiewicz** - *Initial work* - [GitHub](https://github.com/greg-marcin-sienkiewicz)


## Acknowledgments

* Jose Portilla for his awesome [Python and Flask Bootcamp: Create Websites using Flask!](https://www.udemy.com/python-and-flask-bootcamp-create-websites-using-flask/) course on Udemy.
