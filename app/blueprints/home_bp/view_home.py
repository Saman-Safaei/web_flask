from flask import session, render_template
from ...database.model.db_model_post import BlogPostDB
from .. import navbar_user_text
from . import blueprint_home


@blueprint_home.route('/', methods=["GET"])
def index():
    post_list = BlogPostDB.query.all()
    return render_template("home.html", post_list=post_list, nav_user_text=navbar_user_text())
