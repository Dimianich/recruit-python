from db import mysql


def create_tables():
    connection = mysql.get_db()    
    cursor = connection.cursor()
    query = "CREATE TABLE IF NOT EXISTS users (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) NOT NULL, password TEXT(1000) NOT NULL)"
    cursor.execute(query)
    query = "CREATE TABLE IF NOT EXISTS data (info TEXT(1000))"
    cursor.execute(query)
    connection.commit()
    cursor.close()
