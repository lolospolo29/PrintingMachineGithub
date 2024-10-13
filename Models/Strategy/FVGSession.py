from Interfaces.Strategy.IStrategy import IStrategy
from Models.StrategyModels.TimeModels.London import LondonOpen


class FVGSession(IStrategy):
    def __init__(self, name):
        self.name = name
        self._TimeWindow = LondonOpen()
        self.level = []
        self.assetNameList = []
        self.entryStrategy = None
        self.exitStrategy = None
        self.pdArrays = []  # Centralized PD array management
        self.safeDataDuration = 3  # Days of Data needed for Strategy

    def addExitStrategy(self, exitStrategy):
        self.exitStrategy = exitStrategy
        # Pass the callback (update_pd_arrays) to the exit strategy
        self.exitStrategy.setCallback(self.updatePDArrays)

    def addEntryStrategy(self, entryStrategy):
        self.entryStrategy = entryStrategy
        # Pass the callback (update_pd_arrays) to the entry strategy
        self.entryStrategy.setCallback(self.updatePDArrays)

    def addAsset(self, assetName):
        self.assetNameList.append(assetName)

    def updatePDArrays(self, newPDArray):
        self.pdArrays.append(newPDArray)

    def isInTime(self):
        if self._TimeWindow.IsInEntryWindow() and self._TimeWindow.IsInExitWindow():
            return True
        return False

    def getExit(self):
        pass

    def getEntry(self):
        pass
