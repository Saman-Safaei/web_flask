from datetime import datetime

from flask import request, redirect, url_for

from ..database.model.db_model_post import BlogPostDB
from ..model.model_code import ResponseCodes
from .. import api, sqlalchemy_db
from flask_restful import Resource, reqparse


class PostsAPI(Resource):

    def post(self):
        title = request.form.get("title", "IDK")
        subtitle = request.form.get("subtitle", "IDK")
        text_body = request.form.get("text_body", "IDK")
        data_to_save = BlogPostDB(title=title, subtitle=subtitle, tags="post;test", text_body=text_body,
                                  creation_time=datetime.now())
        sqlalchemy_db.session.add(data_to_save)
        sqlalchemy_db.session.commit()
        return redirect(url_for('posts.create_post'))


api.add_resource(PostsAPI, "/api/posts")