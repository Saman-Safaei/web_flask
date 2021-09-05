from datetime import timedelta
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from app.jwt_security import identity, authenticate

app = Flask(__name__)
app.secret_key = b"AASas#$^asf$as2!@$fw#efsSAfSDF&@$SAD@$&s/#"
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=20)
app.config['JWT_AUTH_URL_RULE'] = '/refresh_token'
api = Api(app)
jwt = JWT(app, authenticate, identity)
url_list = []

from app import views
from app import page_error_handler
from app.api_folder import api_users
from app.blueprints import posts
app.register_blueprint(posts)
