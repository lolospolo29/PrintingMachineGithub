from collections import deque

import datetime
import pytz


class AssetData:
    def __init__(self, timeFrame):
        self.open = deque(maxlen=60)
        self.high = deque(maxlen=60)
        self.low = deque(maxlen=60)
        self.close = deque(maxlen=60)
        self.time = deque(maxlen=60)
        self.timeStamp = datetime.datetime.now(pytz.utc)
        self.timeFrame = timeFrame

    def addData(self, openPrice, highPrice, lowPrice, closePrice, time):
        """
        Add new OHLC data to the deque.
        """
        self.open.append(openPrice)
        self.high.append(highPrice)
        self.low.append(lowPrice)
        self.close.append(closePrice)
        self.time.append(time)

    def clearData(self):
        """Clears all data from the deques."""
        self.open.clear()
        self.high.clear()
        self.low.clear()
        self.close.clear()
        self.time.clear()
        self.timeStamp = datetime.datetime.now(pytz.utc)

    def toDict(self):
        """Gibt alle Datenpunkte als Dictionary zurück, inklusive timeStamp."""
        # Zeitformatierung: Entfernt Datum und gibt nur die Uhrzeit zurück

        return {
            "AssetData": {
                "timeFrame": self.timeFrame,
                "open": list(self.open),
                "high": list(self.high),
                "low": list(self.low),
                "close": list(self.close),
                "time": list(self.time),  # Formatiert nur die Uhrzeit
                "timeStamp": self.timeStamp  # Zeitstempel im Format ISO
            }
        }
