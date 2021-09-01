from flask import Flask

app = Flask(__name__)

app.run(port=4040, debug=True)
