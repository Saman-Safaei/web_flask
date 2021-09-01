from flask import Flask, render_template

app = Flask(__name__, template_folder="./resources/templates")

@app.route('/')
def home():
    return render_template("home.html")

app.run(port=4040, debug=True)
