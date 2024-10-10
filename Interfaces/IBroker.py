from abc import ABC, abstractmethod


class IBroker(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def getBalance(self):
        pass

    @abstractmethod
    def setLimitOrder(self):
        pass

    @abstractmethod
    def executeMarketOrder(self):
        pass

    @abstractmethod
    def getOrderId(self):
        pass

    @abstractmethod
    def cancelOrder(self):
        pass

    @abstractmethod
    def configureTrade(self):
        pass



