class Order:
    def __init__(self):
        self.status = None
        self.id = None
        self.stopLoss = None
        self.takeProfit = None
        self.riskPercentage = None
        self.broker = None

    def toDict(self):
        """Gibt alle Datenpunkte als Dictionary zurück, inklusive timeStamp."""
        # Zeitformatierung: Entfernt Datum und gibt nur die Uhrzeit zurück

        return {
            "status": self.status,
            "id": self.id,
            "stopLoss": self.stopLoss,
            "takeProfit": self.takeProfit,
            "riskPercentage": self.riskPercentage,
            "broker": self.broker,
        }
