from ..model.model_code import ResponseCodes
from .. import api
from flask_restful import Resource, reqparse


class UsersAPI(Resource):
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

        return {
            "code": ResponseCodes.users_founded,
            "users": []
        }

    def post(self):

        return {"message": ResponseCodes.user_created}

    def delete(self):
        pass

    def put(self):
        pass


api.add_resource(UsersAPI, "/api/users")

