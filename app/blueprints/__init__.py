from flask import Blueprint

posts = Blueprint("posts", __name__, url_prefix="/posts/")

from . import view_posts
