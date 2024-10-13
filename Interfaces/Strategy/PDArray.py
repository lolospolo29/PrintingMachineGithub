from abc import ABC, abstractmethod


class PDArray(ABC):  # Drill Fill CE
    @abstractmethod
    def getArrayList(self):  # return list of possible entrys
        pass

    @abstractmethod
    def getPDArray(self):  # get new Entry
        pass
