from flask import Flask, render_template
from flask_restful import Api, Resource
from classes.api.users_resource import UsersResource

app = Flask(__name__, template_folder="resources/templates")
app.config["SECRET_KEY"] = "asdwaW23Wa235LMgndjc6758FjhktsawfghsdfawvbngrdAdmck23"
api = Api(app)


@app.route('/')
def home():
    return render_template("home.html")


api.add_resource(UsersResource, "/users")


if __name__ == '__main__':
    app.run(port=4040, debug=True)
