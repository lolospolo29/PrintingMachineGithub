class StrategyManager:
    def __init__(self):
        self.strategies = {}

    def registerStrategy(self, strategy):
        self.strategies[strategy.name] = strategy
        print(f"Strategy '{strategy.name}' created and added to the Strategy Manager.")
