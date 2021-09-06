import datetime

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from .jwt_security import identity, authenticate
from flask_sqlalchemy import SQLAlchemy
import os


# APP Creation
app = Flask(__name__)
app.config.from_pyfile(os.path.join(os.path.dirname(__file__), "config_file.py"))
# API Creation
api = Api(app)
# JSON WEB TOKEN Creation
jwt = JWT(app, authenticate, identity)
# SQL ALCHEMY Creation
sqlalchemy_db = SQLAlchemy(app)


# Initialize APIs and Error Handler
from . import page_error_handler
from .api_folder import api_users, api_posts
# Initialize Blueprints
from .blueprints.posts_bp import blueprint_posts
from .blueprints.home_bp import blueprint_home
from .blueprints.users_bp import blueprint_users
# Initialize Models
from .database import model


# Register Blueprints
app.register_blueprint(blueprint_posts)
app.register_blueprint(blueprint_home)
app.register_blueprint(blueprint_users)
