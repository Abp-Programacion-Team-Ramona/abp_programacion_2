import uuid
from usuario_error import UsuarioError


class Usuario:
    ROLES_VALIDOS = ["admin", "usuario", "invitado"]

    def __init__(self, correo: str, nombre: str, contraseña: str, rol: str):
        self.__id = uuid.uuid4()
        self.__correo = correo
        self.__nombre = nombre
        self.__contraseña = contraseña
        self.__rol = rol
        self.__viviendas = []

    # -------- getters ----------
    @property
    def id(self):
        return self.__id

    @property
    def correo(self):
        return self.__correo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def rol(self):
        return self.__rol

    @property
    def viviendas(self):
        return list(self.__viviendas)  # devolver copia defensiva

    # -------- lógica ----------
    def set_contraseña(self, contraseña: str):
        if len(contraseña) < 6:
            raise UsuarioError("La contraseña debe tener al menos 6 caracteres.")
        self.__contraseña = contraseña

    def set_rol(self, rol: str):
        if rol not in self.ROLES_VALIDOS:
            raise UsuarioError(f"Rol inválido. Roles válidos: {self.ROLES_VALIDOS}")
        self.__rol = rol

    def agregar_vivienda(self, vivienda):
        if vivienda in self.__viviendas:
            raise UsuarioError(f"{self.__nombre} ya posee esta vivienda.")
        self.__viviendas.append(vivienda)

    def quitar_vivienda(self, vivienda):
        if vivienda not in self.__viviendas:
            raise UsuarioError(f"{self.__nombre} no posee esta vivienda.")
        self.__viviendas.remove(vivienda)

    def __str__(self):
        return f"Usuario({self.__nombre}, {self.__correo}, rol={self.__rol})"
