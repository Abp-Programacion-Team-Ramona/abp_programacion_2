import uuid


class Vivienda:

    def __init__(self, nombre, id_usuario, calle, altura, piso, nota):
        self._id = uuid.uuid4()
        self._nombre = nombre
        self._id_usuario = id_usuario
        self._calle = calle
        self._altura = altura
        self._piso = piso
        self._nota = nota
        self._dispositivos = []

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre

    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def calle(self):
        return self._calle

    @calle.setter
    def calle(self, nueva_calle):
        self._calle = nueva_calle

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, nueva_altura):
        self._altura = nueva_altura

    @property
    def piso(self):
        return self._piso

    @piso.setter
    def piso(self, nuevo_piso):
        self._piso = nuevo_piso

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nueva_nota):
        self._nota = nueva_nota

    @property
    def dispositivos(self):
        return self._dispositivos

    def agregar_dispositivo(self, dispositivo):
        if dispositivo not in self._dispositivos:
            self._dispositivos.append(dispositivo)
            print(f"Dispositivo agregado a la vivienda {self.nombre}")
        else:
            print(f"El dispositivo '{dispositivo}' ya existe en la vivienda {self.nombre}")

    def quitar_dispositivo(self, dispositivo):
        if dispositivo in self._dispositivos:
            self._dispositivos.remove(dispositivo)
            print(f"Dispositivo eliminado de la vivienda {self.nombre}")
        else:
            print(f"No se encontró el dispositivo '{dispositivo}' en la vivienda {self.nombre}")
