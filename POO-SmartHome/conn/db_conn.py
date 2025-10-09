import mysql.connector
from mysql.connector import errorcode


class DatabaseConnection:
    def connect_to_mysql():
        try:
            return mysql.connector.connect(
                user="root",
                password="localdb",
                host="127.0.0.1",
                database="local",
                port="3306",
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Usuario o Password no válido")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos no existe.")
            else:
                print(err)
        return None
