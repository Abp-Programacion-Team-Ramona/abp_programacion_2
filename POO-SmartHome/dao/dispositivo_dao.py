import uuid
from interfaces import i_dispositivo_dao
from conn.db_conn import DatabaseConnection
from dominio.dispositivo import Dispositivo


class DispositivoDAO(i_dispositivo_dao):
    def __init__(self, db_conn: DatabaseConnection):
        self.db_conn = db_conn.connect_to_mysql()

    def get_dispositivo(self, id: uuid.UUID, tabla_concreta: str, cls):
        conn = self.db_conn
        cursor = conn.cursor()
        query = f"""
        SELECT d.*, h.*
        FROM dispositivos d
        JOIN {tabla_concreta} h ON d.id = h.id
        WHERE d.id = %s
        """
        cursor.execute(query, (str(id),))
        row = cursor.fetchone()
        if row:
            columns = [desc[0] for desc in cursor.description]
            return self.row_to_obj(cls, row, columns)
        return None

    def create_dispositivo(self, dispositivo: Dispositivo):
        conn = self.db_conn
        cursor = conn.cursor()
        query_dispositivos = """
            INSERT INTO dispositivos (id, id_vivienda, nombre_dispositivo, tipo_dispositivo, estado)
            VALUES (%s, %s, %s, %s, %s)
            """
        cursor.execute(
            query_dispositivos,
            (
                str(dispositivo.id),
                str(dispositivo.id_vivienda),
                dispositivo.nombre_dispositivo,
                dispositivo.tipo_dispositivo,
                dispositivo.estado,
            ),
        )
        tabla_concreta = dispositivo.tabla
        columnas_extra = dispositivo.columnas

        values = ", ".join(["%s"] * len(columnas_extra))
        columnas_sql = ", ".join(columnas_extra)

        query_concreta = f"""
            INSERT INTO {tabla_concreta} (id, {columnas_sql})
            VALUES (%s, {values})
            """
        valores = [str(dispositivo.id)] + [
            getattr(dispositivo, c) for c in columnas_extra
        ]
        cursor.execute(query_concreta, valores)

        conn.commit()

    def update_dispositivo(self, dispositivo):
        conn = self.db_conn
        cursor = conn.cursor()
        query_dispositivos = """
            UPDATE dispositivos
            SET nombre_dispositivo = %s,
                tipo_dispositivo = %s,
                estado = %s
            WHERE id = %s
            """
        cursor.execute(
            query_dispositivos,
            (
                dispositivo.nombre_dispositivo,
                dispositivo.tipo_dispositivo,
                dispositivo.estado,
                str(dispositivo.id),
            ),
        )

        tabla_concreta = dispositivo.tabla
        columnas_extra = dispositivo.columnas

        set = ", ".join([f"{c} = %s" for c in columnas_extra])
        query_concreta = f"""
            UPDATE {tabla_concreta}
            SET {set}
            WHERE id = %s
            """

        valores = [getattr(dispositivo, c) for c in columnas_extra] + [
            str(dispositivo.id)
        ]
        cursor.execute(query_concreta, valores)

        conn.commit()

    def delete_dispositivo(self, id: uuid.UUID):
        conn = self.db_conn
        cursor = conn.cursor()
        query = "DELETE FROM dispositivos WHERE id = %s"
        cursor.execute(query, (str(id),))
        conn.commit()

    def row_to_obj(self, cls, row, columns):
        data = dict(zip(columns, row))
        return cls(**data)
