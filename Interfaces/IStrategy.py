from abc import ABC, abstractmethod


class IStrategy(ABC):
    @abstractmethod
    def addAsset(self, assetName):
        pass

    @abstractmethod
    def AddEntryStrategy(self, entryStrategy):
        pass

    @abstractmethod
    def AddExitStrategy(self, entryStrategy):
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

