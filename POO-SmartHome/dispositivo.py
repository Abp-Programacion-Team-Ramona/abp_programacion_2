import uuid
from abc import ABC, abstractmethod


class Dispositivo(ABC):
    def __init__(self, id_vivienda: uuid.UUID, nombre_dispositivo, id_rutina: uuid.UUID = None, rutina=None):
        self.__id = uuid.uuid4()
        self.__nombre_dispositivo = nombre_dispositivo
        self.__id_vivienda = id_vivienda
        self.__id_rutina = id_rutina
        self.__estado = False
        self.__rutina = rutina

    @property
    def id(self):
        return self.__id

    @property
    def nombre_dispositivo(self):
        return self.__nombre_dispositivo

    @property
    def id_vivienda(self):
        return self.__id_vivienda

    @property
    def id_rutina(self):
        return self.__id_rutina

    @property
    def estado(self):
        return self.__estado

    @property
    def rutina(self):
        return self.__rutina

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    def cambiar_nombre_dispositivo(self, nombre):
        if not nombre:
            raise ValueError("El nombre del dispositivo no puede estar vacío")
        self.__nombre_dispositivo = nombre

    def asignar_rutina(self, rutina):
        self.__rutina = rutina
        self.__id_rutina = getattr(rutina, "id", uuid.uuid4())
