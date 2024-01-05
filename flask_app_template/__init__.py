from flask import Flask
from flask_oidc import OpenIDConnect
import sys

from .settings import *
from .utils import create_data_dir

if SECRET_KEY is None:
    sys.stdout.write("Environment variables not found.\nRequired: SECRET_KEY. Is .env file present?")
    exit()

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.config.update({
    'OIDC_CLIENT_SECRETS': 'flask_app_template/keycloak_credentials.json',
    'OIDC_COOKIE_SECURE': False,
    'OIDC_CALLBACK_ROUTE': '/oidc/callback',
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
})
oidc = OpenIDConnect(app)

create_data_dir()

from .views import *