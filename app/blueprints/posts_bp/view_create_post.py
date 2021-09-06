from flask import request, render_template, make_response, session
from flask_restful import abort

from . import blueprint_posts
from .. import navbar_user_text, isUserSigned


@blueprint_posts.route('/create_post')
def create_post():
    if isUserSigned():
        return render_template("create_post.html", nav_user_text=navbar_user_text())
    abort(404)
