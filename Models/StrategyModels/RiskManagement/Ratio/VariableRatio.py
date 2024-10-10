from Interfaces.RiskManagement.IRatio import IRatio


class VariableRatio(IRatio):
    def getRatio(self,stop,takeProfit):
        pass

    def isRatioValid(self):
        return True
