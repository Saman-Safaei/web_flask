import sqlite3


class User:
    def __init__(self, _id: int, username: str, password: str):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        db_connection = sqlite3.connect("app/database/data.db")
        db_cursor = db_connection.cursor()
        query = "SELECT * FROM users WHERE username=?"
        result = db_cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        db_connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        db_connection = sqlite3.connect("app/database/data.db")
        db_cursor = db_connection.cursor()
        query = "SELECT * FROM users WHERE _id=?"
        result = db_cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        db_connection.close()
        return user
