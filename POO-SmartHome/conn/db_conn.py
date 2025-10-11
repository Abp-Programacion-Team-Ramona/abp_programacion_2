import mysql.connector
from mysql.connector import errorcode


class DatabaseConnection:
    @staticmethod
    def connect_to_mysql():
        try:
            connection = mysql.connector.connect(
                user="root",
                password="localdb",
                host="127.0.0.1",
                database="local",
                port="3306",
            )
            print("Conexion exitosa a db")
            return connection

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Usuario o Password no valido")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos no existe.")
            else:
                print(err)
        return None
