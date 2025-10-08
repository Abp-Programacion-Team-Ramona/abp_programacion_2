import uuid
from interfaces import i_dispositivo_dao

TABLAS_VALIDAS = {"aires_acondicionados", "luces", "ventiladores"}


class DispositivoDAO(i_dispositivo_dao):
    def get_dispositivo(self, id: uuid.UUID, tabla_concreta: str, cls):
        if tabla_concreta not in TABLAS_VALIDAS:
            raise ValueError(f"Tabla inválida: {tabla_concreta}")

        with self.__connect_to_mysql() as conn:
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

    def row_to_obj(self, cls, row, columns):
        data = dict(zip(columns, row))
        return cls(**data)
