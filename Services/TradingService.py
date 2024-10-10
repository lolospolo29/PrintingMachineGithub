import datetime

import pytz

from Models.Asset.Asset import Asset

berlin_tz = pytz.timezone('Europe/Berlin')


class TradingService:
    def __init__(self, Monitoring, MongoDBData, MongoDBTrades, DataMapper):
        self._Monitoring = Monitoring
        self._MongoDBData = MongoDBData
        self._MongoDBTrades = MongoDBTrades
        self._DataMapper = DataMapper
        self.assets = {}
        self.openTrades = []

    def createAsset(self, name, strategyName, smtPairName):
        """
        Create a new asset and add it to the controller's asset list.
        """
        asset = Asset(name, strategyName, smtPairName)
        self.assets[name] = asset
        print(f"Asset '{name}' created and added to the controller.")
        return asset

    def addBrokerToAsset(self, asset_name, broker):
        """
        Add a new timeframe to a specific asset.
        """
        if asset_name in self.assets:
            self.assets[asset_name].addBroker(broker)

    def addTimeframeToAsset(self, asset_name, timeframe):
        """
        Add a new timeframe to a specific asset.
        """
        if asset_name in self.assets:
            self.assets[asset_name].addNewTimeFrame(timeframe)

    def addDataToAsset(self, asset_name, timeframe, tradingData):
        """
        Add a new timeframe to a specific asset.
        """
        if asset_name in self.assets:
            self.assets[asset_name].addData(timeframe, tradingData.open, tradingData.high, tradingData.low,
                                            tradingData.close, tradingData.time)

    def addStrategyDataToAsset(self, asset_name, strategyData):
        """
        Add a new timeframe to a specific asset.
        """
        if asset_name in self.assets:
            self.assets[asset_name].addStrategyData(strategyData)

    def handleTradingViewSignal(self, jsonData):

        tradingData = self._DataMapper.MapToClass(jsonData, "tradingData")
        self.addDataToAsset(tradingData.asset, tradingData.timeFrame, tradingData)
        if tradingData.time == "00:00":
            self.openTrades = []
            self.findOpenTrades()
        else:
            self.dailyDataArchive()
            self.RecentDataRetriever()

    def handleTrades(self):
        pass
        # for trade in Trades:
        #     strategy = self._StrategyFactory.returnClass(trade.strategy)

    @staticmethod
    def handleExit():
        return None

    @staticmethod
    def handleEntry():
        return None

    def RecentDataRetriever(self):
        for key, asset in self.assets.items():
            current_time = datetime.datetime.now(berlin_tz)
            date_60_days_ago = current_time - datetime.timedelta(days=60)
            strategyDataList = self._MongoDBData.getDataWithinDateRange(asset.name, 'AssetData.timeStamp',
                                                                        date_60_days_ago,
                                                                        current_time)
            for strategyData in strategyDataList:
                mappedStrategyDataClass = self._DataMapper.MapToClass(strategyData, "strategyData")
                self.addStrategyDataToAsset(asset.name,mappedStrategyDataClass)

    def dailyDataArchive(self):
        for key, asset in self.assets.items():
            timeFrames = asset.getAllTimeFrames()
            for timeFrame in timeFrames:
                assetTimeFrameData = asset.timeFrameDataStorageDict(timeFrame)
                self._MongoDBData.add(asset.name, assetTimeFrameData)
            asset.clearAllData()
            current_time = datetime.datetime.now(berlin_tz)
            date_60_days_ago = current_time - datetime.timedelta(days=60)
            self._MongoDBData.deleteOldDocuments(asset.name, 'AssetData.timeStamp', date_60_days_ago)

    def findOpenTrades(self):
        for key, asset in self.assets.items():
            query = self._MongoDBTrades.buildQuery("Trade", "asset", asset.name)  # Setzt den ticker-Wert in das Query

            tradeList = self._MongoDBTrades.find("OpenTrades", query)

            tradeListCount = len(tradeList)

            if tradeListCount == 0:
                self._Monitoring.logInformation("No Trades Open")
            if not tradeListCount < 0:
                self._Monitoring.logInformation("Open Trades")
                for obj in tradeList:
                    self.openTrades.append(self._DataMapper.MapToClass(obj, "Trade"))
        self.removeClosedTrades()

    def removeClosedTrades(self):
        for trade in self.openTrades:
            if trade.status == "closed":
                query = self._MongoDBTrades.buildQuery("Trade", "status", "closed")
                self._MongoDBTrades.deleteByQuery("OpenTrades", query)
                self.openTrades.remove(trade)
        print(self.openTrades)
