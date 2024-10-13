from abc import ABC, abstractmethod


class IStrategy(ABC):
    @abstractmethod
    def addAsset(self, assetName):
        pass

    @abstractmethod
    def addEntryStrategy(self, entryStrategy):
        pass

    @abstractmethod
    def addExitStrategy(self, entryStrategy):
        pass

    @abstractmethod
    def updatePDArrays(self, newPDArray):
        pass

    @abstractmethod
    def isInTime(self):
        pass

    @abstractmethod
    def getEntry(self):
        pass

    @abstractmethod
    def getExit(self):
        pass
