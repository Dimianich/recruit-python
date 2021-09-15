from models.user import UserModel


class UserRepository():

    @staticmethod
    def find_by_username(username):
        connection = mysql.connect()
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = UserModel(*row)
        else:
            user = None
        connection.commit()
        cursor.close()
        return user

    @staticmethod
    def find_by_id(_id):
        connection = mysql.connect()
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = UserModel(*row)
        else:
            user = None
        connection.commit()
        cursor.close()
        return user

    @staticmethod
    def save_to_db(username, password):
        connection = mysql.connect()
        cursor = connection.cursor()
        query = "INSERT INTO users(username, password) VALUES (?, ?)"
        cursor.execute(query, (username, password))
        connection.commit()
        cursor.close()
