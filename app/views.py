from flask import render_template, request
from app import app, url_list
from app.model.model_post import BlogPost

url_list.append(BlogPost("Home Page", "1400/6/12", "This is a body Text test", "/"))


@app.route('/', methods=["GET"])
def hello_world():
    print(request.cookies.get("name_key", "SSS"))
    return render_template("home.html", post_list=url_list)
