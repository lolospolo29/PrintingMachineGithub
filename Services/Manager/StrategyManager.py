class StrategyManager:
    def __init__(self):
        self.strategies = {}

    def registerStrategy(self, strategy, name):
        self.strategies[name] = strategy
        print(f"Strategy '{name}' created and added to the Strategy Manager.")

    def addAssetToStrategy(self, assetName, strategyName):
        if strategyName in self.strategies:
            self.strategies[strategyName].addAsset(assetName)
