from ... import sqlalchemy_db


class BlogPostDB(sqlalchemy_db.Model):
    _id = sqlalchemy_db.Column(sqlalchemy_db.INTEGER, primary_key=True, autoincrement=True)
    title = sqlalchemy_db.Column(sqlalchemy_db.TEXT)
    subtitle = sqlalchemy_db.Column(sqlalchemy_db.TEXT)
    tags = sqlalchemy_db.Column(sqlalchemy_db.TEXT)
    text_body = sqlalchemy_db.Column(sqlalchemy_db.TEXT)
    creation_time = sqlalchemy_db.Column(sqlalchemy_db.DATETIME)

