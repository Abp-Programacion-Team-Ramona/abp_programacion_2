import mysql.connector
from mysql.connector import errorcode


class DatabaseConnection:
    @staticmethod
    def connect_to_mysql():
        try:
            connection = mysql.connector.connect(
                user="root",
                password="localdb",
                host="localhost",
                database="abp_db",
                port="3306",
            )
            return connection

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Usuario o Password no valido")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos no existe.")
            else:
                print(err)
        return None
