from ... import sqlalchemy_db


class UserDB(sqlalchemy_db.Model):
    _id = sqlalchemy_db.Column(sqlalchemy_db.INTEGER, primary_key=True, autoincrement=True)
    username = sqlalchemy_db.Column(sqlalchemy_db.TEXT, unique=True)
    e_mail = sqlalchemy_db.Column(sqlalchemy_db.TEXT, unique=True)
    password = sqlalchemy_db.Column(sqlalchemy_db.TEXT)
