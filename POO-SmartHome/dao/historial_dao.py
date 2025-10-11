import uuid
from dao.interfaces.i_historial_dao import IHistorialDAO
from conn.db_conn import DatabaseConnection
from dominio.historial import Historial


class HistorialDAO(IHistorialDAO):
    def __init__(self, db_conn: DatabaseConnection):
        self.db_conn = db_conn.connect_to_mysql()

    def get(self, id: uuid.UUID) -> Historial:
        conn = self.db_conn
        cursor = conn.cursor()
        query = """
        select * from historiales
        where id =%s
        """
        cursor.execute(query, (str(id),))
        row = cursor.fetchone()
        if row:
            return Historial(
                row[0],
                row[1],
                row[2],
                row[3],
            )
        return None

    def create(self, historial: Historial) -> bool:
        conn = self.db_conn
        cursor = conn.cursor()
        query = """
        INSERT INTO historiales (id, id_dispositivo,fecha,descripcion)
        VALUES (%s, %s, %s, %s)
        """
        try:
            cursor.execute(
                query,
                (
                    str(historial.id),
                    historial.id_dispositivo,
                    historial.fecha,
                    historial.descripcion,
                ),
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al crear historial: {e}")
            conn.rollback()
            return False
