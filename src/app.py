from flask import Flask, render_template
from flask_restful import Api, Resource

app = Flask(__name__, template_folder="resources/templates")
app.config["SECRET_KEY"] = "asdwaW23Wa235LMgndjc6758Fjhktmck23"


@app.route('/')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(port=4040, debug=True)
