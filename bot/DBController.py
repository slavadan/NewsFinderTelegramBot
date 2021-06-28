from sqlite3 import *


class DBController:

    def __init__(self, database):
        self.connection = connect(database)
        self.cursor = self.connection.cursor()

    def check_user(self, user_id: int):
        result = self.cursor.execute(f"SELECT * FROM users WHERE user_id = {user_id}").fetchall()
        return bool(len(result))

    def add_user(self, user_id):
        self.cursor.execute(f"INSERT INTO users (user_id, `status`) VALUES({user_id}, {1})")
        self.connection.commit()

    def get_all(self):
        result = self.cursor.execute(f"SELECT * FROM users").fetchall()
        return result

    def close(self):
        self.connection.close()
