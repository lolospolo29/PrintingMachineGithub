
class AssetManager:
    def __init__(self):
        self.assets = {}

    def addAsset(self, asset):
        self.assets[asset.name] = asset
        print(f"Asset '{asset.name}' created and added to Asset Manager.")

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

    def returnAssets(self):
        return self.assets
