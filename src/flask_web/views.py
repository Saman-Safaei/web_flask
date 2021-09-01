from flask import render_template
from flask_web import app

listed = []
for a in range(1, 101):
    listed.append(f"Hello World {a}")


@app.route('/')
def index():
    return render_template("Home.html", title="Home", paragraphs=listed)
