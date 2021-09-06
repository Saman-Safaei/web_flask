from flask import render_template, request, abort, redirect, url_for, session
from . import blueprint_users, sqlalchemy_db
from ...database.model.db_model_user import UserDB


@blueprint_users.route("signup", methods=['GET', 'POST'])
def sign_up_user():
    return render_template("signup.html")


@blueprint_users.route("login", methods=['GET', 'POST'])
def login_user():
    if request.method == "POST":
        u_name = request.form.get("username", None)
        u_pass = request.form.get("password", None)
        if not u_name or not u_pass:
            return redirect(url_for("users.login_user"))
        user = UserDB.query.filter_by(username=u_name).first()
        if user:
            if u_pass == user.password:
                session["signed_user"] = u_name
                session["signed_password"] = u_pass
        return redirect(url_for("home.index"))

    return render_template("login.html")
