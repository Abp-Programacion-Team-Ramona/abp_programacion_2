import uuid


class Usuario:
    ROLES_VALIDOS = ["admin", "usuario", "invitado"]

    def __init__(self, id: uuid.UUID, correo: str, nombre: str, contraseña: str, rol: str):
        self.__id = id
        self.__correo = correo
        self.__nombre = nombre
        self.__contraseña = contraseña
        self.__rol = rol
        self.__viviendas = []

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

    def cambiar_contraseña(self):
        success = False
        while not success:
            print("Indique la nueva contraseña (mínimo 6 caracteres)")
            contraseña = input()
            if len(contraseña) >= 6:
                self.__contraseña = contraseña
                success = True
            else:
                print("La contraseña debe tener al menos 6 caracteres")

    def cambiar_rol(self):
        success = False
        while not success:
            print(f"Indique el nuevo rol: {', '.join(self.ROLES_VALIDOS)}")
            rol = input().lower()
            if rol in self.ROLES_VALIDOS:
                self.__rol = rol
                success = True
            else:
                print(f"El rol '{rol}' es inválido. Roles válidos: {', '.join(self.ROLES_VALIDOS)}")

    def cambiar_correo(self):
        success = False
        while not success:
            print("Indique el nuevo correo electrónico")
            correo = input()
            if "@" in correo and "." in correo:
                self.__correo = correo
                success = True
            else:
                print("El correo debe contener '@' y '.'")

    def cambiar_nombre(self):
        success = False
        while not success:
            print("Indique el nuevo nombre")
            nombre = input().strip()
            if len(nombre) > 0:
                self.__nombre = nombre
                success = True
            else:
                print("El nombre no puede estar vacío")

    def agregar_vivienda(self):
        success = False
        while not success:
            print("Indique el ID de la vivienda a agregar")
            vivienda_id = input()
            if vivienda_id in self.__viviendas:
                print(f"{self.__nombre} ya posee esta vivienda.")
            else:
                self.__viviendas.append(vivienda_id)
                success = True

    def quitar_vivienda(self):
        success = False
        while not success:
            print("Indique el ID de la vivienda a quitar")
            vivienda_id = input()
            if vivienda_id not in self.__viviendas:
                print(f"{self.__nombre} no posee esta vivienda.")
            else:
                self.__viviendas.remove(vivienda_id)
                success = True

    def __str__(self):
        return f"Usuario({self.__nombre}, {self.__correo}, rol={self.__rol})"