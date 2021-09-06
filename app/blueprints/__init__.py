from flask import session
from ..database.model.db_model_user import UserDB


def navbar_user_text():
    username = session.get("signed_user", None)
    password = session.get("signed_password", None)
    if username and password:
        user = UserDB.query.filter_by(username=username).first()
        if password == user.password:
            return username
    return "Login / SignUp"


def isUserSigned():
    username = session.get("signed_user", None)
    password = session.get("signed_password", None)
    if username and password:
        user = UserDB.query.filter_by(username=username).first()
        if password == user.password:
            return True
    return False

