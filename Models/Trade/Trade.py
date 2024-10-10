class Trade:

    def __init__(self,asset,strategyName):
        self.status = None
        self.asset = asset
        self.orders = []
        self.strategyName = strategyName
        self.pnl = 0
