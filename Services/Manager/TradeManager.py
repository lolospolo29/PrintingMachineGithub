class TradeManager:
    def __init__(self, AssetManager, StrategyManager, MongoDBTrades, Monitoring, DataMapper):
        self.openTrades = []
        self._AssetManager = AssetManager
        self._StrategyManager = StrategyManager
        self._MongoDBTrades = MongoDBTrades
        self._Monitoring = Monitoring
        self._DataMapper = DataMapper

    def clearOpenTrades(self):
        self.openTrades = []

    def findOpenTrades(self):
        assets = self._AssetManager.returnAssets()

        # Iterate over the assets
        for key, asset in assets.items():
            query = self._MongoDBTrades.buildQuery("Trade", "asset", asset.name)  # Setzt den ticker-Wert in das Query

            tradeList = self._MongoDBTrades.find("OpenTrades", query)

            tradeListCount = len(tradeList)

            if tradeListCount == 0:
                self._Monitoring.logInformation("No Trades Open")
            if not tradeListCount < 0:
                for obj in tradeList:
                    self.openTrades.append(self._DataMapper.MapToClass(obj, "Trade"))
        self.archiveClosedTrades()

    def archiveClosedTrades(self):
        for trade in self.openTrades:
            if trade.status == "closed":
                query = self._MongoDBTrades.buildQuery("Trade", "status", "closed")
                self._MongoDBTrades.deleteByQuery("OpenTrades", query)
                tradeData = trade.toDict()
                self._MongoDBTrades.add("ClosedTrades", tradeData)
                self.openTrades.remove(trade)
