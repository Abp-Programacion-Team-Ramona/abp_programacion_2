import uuid
from abc import ABC, abstractmethod


class Dispositivo(ABC):
    def _init_(self, id_vivienda: uuid.UUID, id_rutina: uuid.UUID = None, rutina=None):
        self._id = uuid.uuid4()
        self._id_vivienda = id_vivienda
        self._id_rutina = id_rutina
        self._estado = False
        self._rutina = rutina

    @property
    def id(self):
        return self._id

    @property
    def id_vivienda(self):
        return self._id_vivienda

    @property
    def id_rutina(self):
        return self._id_rutina

    @property
    def estado(self):
        return self._estado

    @property
    def rutina(self):
        return self._rutina

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    def asignar_rutina(self, rutina):
        self._rutina = rutina
        self._id_rutina = getattr(rutina, "id", uuid.uuid4())