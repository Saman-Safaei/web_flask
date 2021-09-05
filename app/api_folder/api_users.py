from flask_jwt import jwt_required
from app.model.model_code import ResponseCodes
from app import api, url_list
import sqlite3
from flask_restful import Resource, reqparse
from app.model.model_users import User
from app.model.model_post import BlogPost


class Users(Resource):
    # json require some fields
    parser = reqparse.RequestParser()

    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="Username field cannot be blank !"
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="Password field cannot be blank !"
    )
    # json require some fields

    def get(self):
        db_conn = sqlite3.connect("app/database/data.db")
        db_cursor = db_conn.cursor()
        query = "SELECT * FROM users"
        users = list(db_cursor.execute(query).fetchall())
        user_list = []
        for user in users:
            user_list.append({
                "id": user[0],
                "username": user[1],
                "password": user[2]
            })
        return {
            "code": ResponseCodes.users_founded,
            "users": user_list
        }

    def post(self):
        data = Users.parser.parse_args()
        user = User.find_by_username(data["username"])
        if user is not None:
            return {"message": ResponseCodes.user_exists}, 403
        db_conn = sqlite3.connect("app/database/data.db")
        db_cursor = db_conn.cursor()
        query = "INSERT INTO users VALUES (NULL , ? , ?)"
        db_cursor.execute(query, (data["username"], data["password"]))
        db_conn.commit()
        db_conn.close()
        return {"message": ResponseCodes.user_created}

    def delete(self):
        pass

    def put(self):
        pass


api.add_resource(Users, "/api/users")
url_list.append(BlogPost("User Api", "1400/6/12", "This is a body Text<h1>Hello</h1> test", "/api/users"))

