from flask_restful import Api, Resource
import sqlite3


class UsersResource(Resource):
    def get(self):
        return {"message": "Users"}
