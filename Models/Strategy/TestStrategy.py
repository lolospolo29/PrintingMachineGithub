from Interfaces.IStrategy import IStrategy
from Models.StrategyModels.TimeModels.London import LondonOpen


class TestStrategy(IStrategy):
    def __init__(self, name):
        self.name = name
        self._TimeWindow = LondonOpen()
        self.level = []
        self.safeDataDuration = 3 # Days of Data needed for Strategy

    def isInTime(self):
        if self._TimeWindow.IsInEntryWindow() and self._TimeWindow.IsInExitWindow():
            return True
        return False

    def CalculateLevels(self):
        pass

    def isStrategyValid(self):
        pass

    def getExit(self):
        pass

    def getEntry(self):
        pass
