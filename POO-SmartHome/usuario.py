import uuid
from usuario_error import UsuarioError

class Usuario:
    ROLES_VALIDOS = ["admin", "usuario", "invitado"]

    def __init__(self, correo: str, nombre: str, contraseña: str, rol: str = "usuario"):
        self.id = uuid.uuid4()
        self.correo = correo
        self.nombre = nombre
        self.set_contraseña(contraseña)
        self.set_rol(rol)
        self.viviendas = []

    def set_contraseña(self, contraseña: str):
        if len(contraseña) < 6:
            raise UsuarioError("La contraseña debe tener al menos 6 caracteres.")
        self.contraseña = contraseña

    def set_rol(self, rol: str):
        if rol not in self.ROLES_VALIDOS:
            raise UsuarioError(f"Rol inválido. Roles válidos: {self.ROLES_VALIDOS}")
        self.rol = rol

    def agregar_vivienda(self, vivienda):
        if vivienda in self.viviendas:
            raise UsuarioError(f"{self.nombre} ya posee esta vivienda.")
        self.viviendas.append(vivienda)

    def quitar_vivienda(self, vivienda):
        if vivienda not in self.viviendas:
            raise UsuarioError(f"{self.nombre} no posee esta vivienda.")
        self.viviendas.remove(vivienda)

    def __str__(self):
        return f"Usuario({self.nombre}, {self.correo}, rol={self.rol})"

