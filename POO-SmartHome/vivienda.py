import uuid


class Vivienda:

    def __init__(self, nombre, id_usuario, calle, altura, piso, nota):
        self.__id = uuid.uuid4()
        self.__nombre = nombre
        self.__id_usuario = id_usuario
        self.__calle = calle
        self.__altura = altura
        self.__piso = piso
        self.__nota = nota
        self.__dispositivos = []

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 0:
            self.__nombre = nuevo_nombre

    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def calle(self):
        return self.__calle

    @calle.setter
    def calle(self, nueva_calle):
        self.__calle = nueva_calle

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, nueva_altura):
        self.__altura = nueva_altura

    @property
    def piso(self):
        return self.__piso

    @piso.setter
    def piso(self, nuevo_piso):
        self.__piso = nuevo_piso

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nueva_nota):
        self.__nota = nueva_nota

    @property
    def dispositivos(self):
        return self.__dispositivos

    def agregar_dispositivo(self, dispositivo):
        if dispositivo not in self.__dispositivos:
            self.__dispositivos.append(dispositivo)
            print(f"Dispositivo agregado a la vivienda {self.nombre}")
        else:
            print(f"El dispositivo '{dispositivo}' ya existe en la vivienda {self.nombre}")

    def quitar_dispositivo(self, dispositivo):
        if dispositivo in self.__dispositivos:
            self.__dispositivos.remove(dispositivo)
            print(f"Dispositivo eliminado de la vivienda {self.nombre}")
        else:
            print(f"No se encontró el dispositivo '{dispositivo}' en la vivienda {self.nombre}")
