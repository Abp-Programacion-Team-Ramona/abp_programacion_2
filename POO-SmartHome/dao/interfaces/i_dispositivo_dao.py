import uuid
from abc import ABC, abstractmethod


class IDispositivoDAO(ABC):
    @abstractmethod
    def get(self, id: uuid.UUID, tabla_concreta: str, cls):
        pass

    @abstractmethod
    def create(self, object):
        pass

    @abstractmethod
    def update(self, object):
        pass

    @abstractmethod
    def delete(self, object):
        pass
