from abc import ABC, abstractmethod


class IRegistryFactory(ABC):

    # Abstract method: must be implemented by subclasses
    @abstractmethod
    def registerClass(self):
        pass

    @abstractmethod
    def returnRegistryClass(self):
        pass
