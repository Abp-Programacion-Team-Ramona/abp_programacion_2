import uuid

class Historial:
    def __init__(self, id, id_dispositivo, fecha, descripcion):
        self.__id = id
        self.__id_dispositivo = id_dispositivo
        self.__fecha = fecha
        self.__descripcion = descripcion

    @property
    def id(self):
        return self.__id

    @property
    def id_dispositivo(self):
        return self.__id_dispositivo

    @property
    def fecha(self):
        return self.__fecha

    @property
    def descripcion(self):
        return self.__descripcion
        
