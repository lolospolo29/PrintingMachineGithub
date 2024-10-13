class strategyData:  # DITO AssetData from DB
    def __init__(self, timeStamp, timeFrame):
        self.open = []
        self.high = []
        self.low = []
        self.close = []
        self.timeStamp = timeStamp
        self.timeFrame = timeFrame
