from flask import Blueprint

blueprint_posts = Blueprint("posts", __name__, url_prefix="/posts/")

from . import view_posts, view_create_post, view_show_post
