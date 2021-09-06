from datetime import timedelta
import os


SECRET_KEY = b"AASas#$^as*fsAad&aw$as2!@$fw#efsSAfSDF&@$SAD@$&s/#"
JWT_EXPIRATION_DELTA = timedelta(seconds=20)
JWT_AUTH_URL_RULE = '/refresh_token'
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(os.path.dirname(__file__), "database", "data.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
