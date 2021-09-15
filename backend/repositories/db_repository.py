from repositories.abstract_data_repository import AbstractDataRepository


class DbRepository(AbstractDataRepository):

    def get_all(self):
        connection = mysql.connect()
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
        connection = mysql.connect()
        cursor = connection.cursor()
        query = "INSERT INTO data VALUES(?)"
        cursor.execute(query, (info,))
        connection.commit()
        cursor.close()
