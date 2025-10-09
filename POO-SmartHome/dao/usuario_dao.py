import uuid
from interfaces import i_usuario_dao
from conn.db_conn import DatabaseConnection
from dominio.usuario import Usuario


class UsuarioDAO(i_usuario_dao):
    def __init__(self, db_conn: DatabaseConnection):
        self.db_conn = db_conn.connect_to_mysql()

    def get_usuario(self, id: uuid.UUID) -> Usuario:
        conn = self.db_conn
        cursor = conn.cursor()
        query = """
        SELECT id, correo, nombre, contraseña, rol
        FROM usuarios
        WHERE id = %s
        """
        cursor.execute(query, (str(id),))
        row = cursor.fetchone()
        if row:
            return Usuario(correo=row[1], nombre=row[2], contraseña=row[3], rol=row[4])
        return None

    def create_usuario(self, usuario: Usuario) -> bool:
        conn = self.db_conn
        cursor = conn.cursor()
        query = """
        INSERT INTO usuarios (id, correo, nombre, contraseña, rol)
        VALUES (%s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(
                query,
                (
                    str(usuario.id),
                    usuario.correo,
                    usuario.nombre,
                    usuario.contraseña,
                    usuario.rol,
                ),
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            conn.rollback()
            return False

    def update_usuario(self, usuario: Usuario) -> bool:
        conn = self.db_conn
        cursor = conn.cursor()
        query = """
        UPDATE usuarios
        SET correo = %s,
            nombre = %s,
            contraseña = %s,
            rol = %s
        WHERE id = %s
        """
        try:
            cursor.execute(
                query,
                (
                    usuario.correo,
                    usuario.nombre,
                    usuario.contraseña,
                    usuario.rol,
                    str(usuario.id),
                ),
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            conn.rollback()
            return False

    def delete_usuario(self, id: uuid.UUID) -> bool:
        conn = self.db_conn
        cursor = conn.cursor()
        query = "DELETE FROM usuarios WHERE id = %s"
        try:
            cursor.execute(query, (str(id),))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            conn.rollback()
            return False

    def row_to_obj(self, row):
        return Usuario(correo=row[1], nombre=row[2], contraseña=row[3], rol=row[4])
