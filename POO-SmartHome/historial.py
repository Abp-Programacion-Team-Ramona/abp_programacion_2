import uuid

class Historial:
    def __init__(self,id_dispositivo,fecha,descripcion):
        self.__id=uuid.uuid4()
        self.__id_dispositivo=id_dispositivo
        self.__fecha=fecha
        self.__descripcion=descripcion

    @property
    def id(self):
        return self.__id

    @property
    def id_dispositivo(self):
        return self.__id_dispositivo

    @property
    def fecha(self):
        return self.fecha

    @property
    def descripcion(self):
        return self.descripcion
