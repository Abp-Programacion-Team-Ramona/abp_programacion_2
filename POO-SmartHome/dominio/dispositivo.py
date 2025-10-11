import uuid
from abc import ABC, abstractmethod


class Dispositivo(ABC):
    tabla = None
    columnas = []

    def __init__(
        self,
        id: uuid,
        id_vivienda: uuid,
        nombre_dispositivo: str,
        tipo_dispositivo: str,
        estado: bool,
        **kwargs,
    ):
        self._id = id
        self._id_vivienda = id_vivienda
        self._nombre_dispositivo = nombre_dispositivo
        self._tipo_dispositivo = tipo_dispositivo
        self._estado = estado
        self._rutina = None

    @property
    def id(self):
        return self.__id

    @property
    def nombre_dispositivo(self):
        return self.__nombre_dispositivo

    @property
    def tipo_dispositivo(self):
        return self.tipo_dispositivo

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
