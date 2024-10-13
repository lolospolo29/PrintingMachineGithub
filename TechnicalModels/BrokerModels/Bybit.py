from Interfaces.IBroker import IBroker


class Bybit(IBroker):

    def __init__(self, name):
        self._name = name

    def configureTrade(self):
        pass

    def cancelOrder(self):
        pass

    def getOrderId(self):
        pass

    def executeMarketOrder(self):
        pass

    def setLimitOrder(self):
        pass

    def getBalance(self):
        pass

    @property
    def name(self):
        return self._name
