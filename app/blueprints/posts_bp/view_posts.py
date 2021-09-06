from . import blueprint_posts


@blueprint_posts.route("/")
def posts_home():
    return "This is a page"
