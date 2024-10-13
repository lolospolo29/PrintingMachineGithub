class Trade:

    def __init__(self, asset, strategyName):
        self.status = None
        self.asset = asset
        self.orders = []
        self.strategyName = strategyName
        self.pnl = 0

    def toDict(self):
        """Gibt alle Datenpunkte als Dictionary zurück, inklusive timeStamp."""
        # Zeitformatierung: Entfernt Datum und gibt nur die Uhrzeit zurück

        return {
            "Trade": {
                "status": self.status,
                "asset": self.asset,
                "orders": [order.toDict() for order in self.orders],  # Convert each order to a dict
                "strategyName": self.strategyName,
                "pnl": self.pnl,
            }
        }
