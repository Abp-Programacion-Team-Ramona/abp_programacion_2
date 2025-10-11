import uuid
from abc import ABC, abstractmethod


class IUsuarioDAO(ABC):
    @abstractmethod
    def get(self, id: uuid):
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
