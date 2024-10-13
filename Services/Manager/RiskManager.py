class RiskManager:
    def __init__(self,maxDrawdown,RiskPerTrade):
        self.maxDrawdown = maxDrawdown  # Maximaler Verlust in %
        self.riskPerTrade = RiskPerTrade  # Prozentuales Risiko pro Trade
        self.currentDrawdown = 0.0  # Aktueller Drawdown

    # def setRiskStrategy(self,strategy,name):
    #     return None
    # def setStopLossStrategy(self,strategy,name):
    #     return None
    def setNewsTime(self,time):
        return None
    def setRiskPerTrade(self,percent):
        return None
    def getRiskPerTrade(self):
        return None
    def setcurrentDrawdown(self,drawdown):
        return None



