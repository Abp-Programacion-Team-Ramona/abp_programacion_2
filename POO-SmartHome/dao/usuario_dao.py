import uuid
from interfaces import i_usuario_dao
from conn.db_conn import DatabaseConnection
from dominio.usuario import Usuario


class UsuarioDAO(i_usuario_dao):
    def __init__(self, db_conn: DatabaseConnection):
        self.db_conn = db_conn.connect_to_mysql()

    def get_usuario(self, user: str, contrasena: str) -> Usuario:
        conn = self.db_conn
        cursor = conn.cursor()
        query = """
        SELECT id, correo, nombre, contrasena, rol
        FROM usuarios
        WHERE nombre = %s
        and contrasena = %s
        """
        cursor.execute(query, (user, contrasena))
        row = cursor.fetchone()
        if row:
            return Usuario(
                id=row[0], correo=row[1], nombre=row[2], contrasena=row[3], rol=row[4]
            )
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
                    usuario.contrasena,
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
                    usuario.contrasena,
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

    def update_usuario_rol(self, correo: str, rol: str) -> bool:
        conn = self.db_conn
        cursor = conn.cursor()
        query = """
        UPDATE usuarios
        SET   rol = %s
        WHERE correo = %s
        """
        try:
            cursor.execute(
                query,
                (
                    rol,
                    correo,
                ),
            )
            conn.commit()
            print(f"Actualizado el rol del usuario a {rol}")
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
