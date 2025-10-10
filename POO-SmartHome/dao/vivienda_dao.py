import uuid
from interfaces import i_vivienda_dao
from conn.db_conn import DatabaseConnection
from dominio.vivienda import Vivienda


class ViviendaDAO(i_vivienda_dao):
    def __init__(self, db_conn: DatabaseConnection):
        self.db_conn = db_conn.connect_to_mysql()

    def get_vivienda(self, id: uuid.UUID) -> Vivienda:
        conn = self.db_conn
        cursor = conn.cursor()
        query = """
        SELECT * FROM viviendas
        WHERE id = %s
        """
        cursor.execute(query, (str(id),))
        row = cursor.fetchone()
        if row:
            return Vivienda(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
            )
        return None

    def create_vivienda(self, vivienda: Vivienda) -> bool:
        conn = self.db_conn
        cursor = conn.cursor()
        query = """
        INSERT INTO viviendas (id, nombre, id_usuario, calle, altura,piso,nota)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(
                query,
                (
                    str(vivienda.id),
                    vivienda.nombre,
                    vivienda.id_usuario,
                    vivienda.calle,
                    vivienda.altura,
                    vivienda.piso,
                    vivienda.nota,
                ),
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al crear vivienda: {e}")
            conn.rollback()
            return False

    def update_usuario(self, vivienda: Vivienda) -> bool:
        conn = self.db_conn
        cursor = conn.cursor()
        query = """
        UPDATE viviendas
        SET nombre = %s,
            id_usuario = %s,
            calle = %s,
            altura= %s,
            piso = %s,
            nota = %s
        WHERE id = %s
        """
        try:
            cursor.execute(
                query,
                (
                    vivienda.nombre,
                    vivienda.id_usuario,
                    vivienda.calle,
                    vivienda.altura,
                    vivienda.piso,
                    vivienda.nota,
                    str(vivienda.id),
                ),
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar vivienda: {e}")
            conn.rollback()
            return False

    def delete_usuario(self, id: uuid.UUID) -> bool:
        conn = self.db_conn
        cursor = conn.cursor()
        query = "DELETE FROM viviendas WHERE id = %s"
        try:
            cursor.execute(query, (str(id),))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar vivienda: {e}")
            conn.rollback()
            return False
