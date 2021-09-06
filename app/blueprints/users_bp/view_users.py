from flask import redirect, url_for
from . import blueprint_users, sqlalchemy_db
from .. import isUserSigned


@blueprint_users.route("/")
def user_home():
    is_signed = isUserSigned()
    print(is_signed)
    if not is_signed:
        return redirect(url_for('users.login_user'))
    return "PLEASE WAIT FOR THIS - THIS IS USER DASHBOARD"
