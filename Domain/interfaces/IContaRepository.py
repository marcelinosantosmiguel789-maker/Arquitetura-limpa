from abc import ABC, abstractmethod

class IContaRepository(ABC):
    @abstractmethod
    def create(self, conta):
        pass

    @abstractmethod
    def read(self, id_conta):
        pass

    @abstractmethod
    def update(self, conta):
        pass

    @abstractmethod
    def delete(self, id_conta):
        pass