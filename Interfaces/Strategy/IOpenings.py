from abc import ABC, abstractmethod


class IOpenings(ABC):  # Opening Gap
    @abstractmethod
    def getLevels(self):  # return List of all NDOG / NWOG
        pass

