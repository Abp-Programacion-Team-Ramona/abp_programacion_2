import uuid
from abc import ABC, abstractmethod


class IDispositivoDAO(ABC):
    @abstractmethod
    def get(self, id: uuid):
        pass

    @abstractmethod
    def create(self, object):
        pass