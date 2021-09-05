import datetime

from flask import request, render_template, make_response
from . import posts
from .. import url_list
from ..model.model_post import BlogPost


@posts.route("/")
def posts_home():
    return "This is a page"


@posts.route('/<string:username>/create_post', methods=["GET", "POST"])
def create_post(username):
    if request.method == "POST":
        title = request.form.get("title", "IDK")
        subtitle = request.form.get("subtitle", "IDK")
        text_body = request.form.get("text_body", "IDK")
        url_list.append(BlogPost(title, subtitle, text_body, '/?'))
        response = make_response(render_template("create_post.html", username=username))
        response.set_cookie("name_key", "Cookie Set", max_age=datetime.timedelta(seconds=128))
        return response
    return render_template("create_post.html", username=username)
