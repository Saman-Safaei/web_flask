from flask import render_template
from . import blueprint_posts
from ...database.model.db_model_post import BlogPostDB
from .. import navbar_user_text


@blueprint_posts.route("/<int:_id>")
def show_a_post(_id):
    post = BlogPostDB.query.filter_by(_id=_id).first_or_404()
    return render_template("show_a_post.html", blog_post=post, nav_user_text=navbar_user_text())
