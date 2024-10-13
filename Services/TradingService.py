import datetime
import time

import pytz

ny_tz = pytz.timezone('America/New_York')


class TradingService:
    def __init__(self, Monitoring, MongoDBData, MongoDBTrades, DataMapper, StrategyManager, AssetManager, TradeManager):
        self._Monitoring = Monitoring
        self._MongoDBData = MongoDBData
        self._MongoDBTrades = MongoDBTrades
        self._DataMapper = DataMapper
        self._StrategyManager = StrategyManager
        self._AssetManager = AssetManager
        self._TradeManager = TradeManager
        self.lock_active = False  # Flag um den Status des Locks zu verfolgen

    def handleTradingViewSignal(self, jsonData):

        tradingData = self._DataMapper.MapToClass(jsonData, "tradingData")
        self._AssetManager.addDataToAsset(tradingData.asset, tradingData.timeFrame, tradingData)
        trading_time_utc = datetime.datetime.strptime(tradingData.time, "%H:%M")

        # Prüfen, ob trading_time_ny gleich Mitternacht ist (00:00)
        if trading_time_utc.strftime("%H:%M") == "04:00":
            if not self.lock_active:  # Nur wenn der Lock nicht aktiv ist
                self.lock_active = True  # Lock aktivieren
                # Dies wird nur einmal um 04:00 Uhr ausgeführt
                self._TradeManager.clearOpenTrades()
                self._TradeManager.findOpenTrades()
                self.lock_active = False  # Lock wieder deaktivieren nach der Ausführung

            else:
                while self.lock_active:
                    time.sleep(1)
        else:
            while self.lock_active:
                time.sleep(1)
            self.dailyDataArchive()
            self.RecentDataRetriever()

    def RecentDataRetriever(self):
        assets = self._AssetManager.returnAssets()

        # Iterate over the assets
        for key, asset in assets.items():
            current_time_ny = datetime.datetime.now(ny_tz)

            # Berechne das Datum von vor 60 Tagen in der New Yorker Zeitzone
            date_60_days_ago_ny = current_time_ny - datetime.timedelta(days=60)

            # Umwandlung beider Zeiten in UTC
            current_time_utc = current_time_ny.astimezone(pytz.utc)
            date_60_days_ago_utc = date_60_days_ago_ny.astimezone(pytz.utc)

            strategyDataList = self._MongoDBData.getDataWithinDateRange(asset.name, 'AssetData.timeStamp',
                                                                        date_60_days_ago_utc,
                                                                        current_time_utc)
            for strategyData in strategyDataList:
                mappedStrategyDataClass = self._DataMapper.MapToClass(strategyData, "strategyData")
                self._AssetManager.addStrategyDataToAsset(asset.name, mappedStrategyDataClass)

    def dailyDataArchive(self):
        assets = self._AssetManager.returnAssets()

        # Iterate over the assets
        for key, asset in assets.items():
            timeFrames = asset.getAllTimeFrames()
            for timeFrame in timeFrames:
                assetTimeFrameData = asset.timeFrameDataToDict(timeFrame)
                self._MongoDBData.add(asset.name, assetTimeFrameData)
            asset.clearAllData()
            current_time_ny = datetime.datetime.now(ny_tz)
            date_60_days_ago_ny = current_time_ny - datetime.timedelta(days=60)
            date_60_days_ago_utc = date_60_days_ago_ny.astimezone(pytz.utc)
            self._MongoDBData.deleteOldDocuments(asset.name, 'AssetData.timeStamp', date_60_days_ago_utc)
