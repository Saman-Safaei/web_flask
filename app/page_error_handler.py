from flask import render_template, request
from . import app


@app.errorhandler(404)
def error_404(error):
    return render_template("error.html",
                           error_head_title="Not Found Error",
                           error_title="404",
                           error_massage="This page doesn't exists !"), 404


@app.errorhandler(500)
def error_500(error):
    return render_template("error.html",
                           error_head_title="Internal Server Error",
                           error_title="500",
                           error_massage="Internal Server Error !")
