from repositories.abstract_data_repository import AbstractDataRepository
from app import mysql


class DbRepository(AbstractDataRepository):

    def get_all(self):
        connection = mysql.get_db()
        cursor = connection.cursor()
        query = "SELECT * FROM data"
        result = cursor.execute(query)
        data = []
        for row in result:
            data.append({"info": row[0]})
        connection.commit()
        cursor.close()
        return data

    def save_data(self, info):
        connection = mysql.get_db()
        cursor = connection.cursor()
        query = "INSERT INTO data VALUES(?)"
        cursor.execute(query, (info,))
        connection.commit()
        cursor.close()
