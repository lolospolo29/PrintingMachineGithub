from Models.Asset.Asset import Asset


class AssetManager:
    def __init__(self):
        self.assets = {}

    def returnAssets(self):
        return self.assets

    def createAsset(self, name, strategyName, smtPairName):
        """
        Create a new asset and add it to the controller's asset list.
        """
        asset = Asset(name, strategyName, smtPairName)
        self.assets[name] = asset
        print(f"Asset '{name}' created and added to the controller.")

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
