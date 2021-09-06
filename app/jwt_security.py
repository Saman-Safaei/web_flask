from .model.model_users import User


def authenticate(username, password):
    user = User.find_by_username(username)
    if user and user.password == password:
        return user


def identity(payload):
    _id = payload['identity']
    user_id = User.find_by_id(_id)
    return user_id
