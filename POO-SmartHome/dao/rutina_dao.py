from interfaces import i_rutina_dao
from conn.db_conn import DatabaseConnection
from dominio.rutina import Rutina


class RutinaDAO(i_rutina_dao):
    def __init__(self, db_conn: DatabaseConnection):
        self.db_conn = db_conn.connect_to_mysql()

    def get_rutina(self, id) -> Rutina:
        conn = self.db_conn
        cursor = conn.cursor()
        query = """
        select * from rutinas r where r.id=%s
        """
        cursor.execute(query, (id))
        row = cursor.fetchone()
        if row:
            return Rutina(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        return None

    def create_rutina(self, rutina: Rutina) -> bool:
        conn = self.db_conn
        cursor = conn.cursor()
        query = """
         insert into rutinas (id,id_dispositivo,descripcion,horario_inicio,horario_apagado,horario_encendido,estado_rutina)
         values(%s,%s,%s,%s,%s,%s,%s)
        """
        try:
            cursor.execute(
                query,
                (
                    str(
                        rutina.id,
                        rutina.id_dispositivo,
                        rutina.descripcion,
                        rutina.horario_inicio,
                        rutina.horario_apagado,
                        rutina.horario_encendido,
                        rutina.estado_rutina,
                    )
                ),
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al crear rutina: {e}")
            conn.rollback()
            return False

    def update_rutina(self, rutina: Rutina):
        conn = self.db_conn
        cursor = conn.cursor()
        query = """
        update rutinas
        set descripcion = %s,
            horario_inicio = %s,
            horario_apagado = %s,
            horario_encendido = %s,
            estado_rutina = %s
        where id = %s
        """
        try:
            cursor.execute(
                query,
                (
                    rutina.descripcion,
                    rutina.horario_inicio,
                    rutina.horario_apagado,
                    rutina.horario_encendido,
                    rutina.estado_rutina,
                    rutina.id,
                ),
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar rutina: {e}")
            conn.rollback()
            return False

    def delete_rutina(self, id):
        conn = self.db_conn
        cursor = conn.cursor()
        query = "DELETE FROM rutinas WHERE id = %s"
        try:
            cursor.execute(query, (str(id),))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar rutina: {e}")
            conn.rollback()
            return False
