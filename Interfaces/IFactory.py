from abc import ABC, abstractmethod


class IFactory(ABC):

    # Abstract method: must be implemented by subclasses
    @abstractmethod
    def returnClass(self):
        pass

