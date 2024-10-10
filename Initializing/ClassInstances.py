from Controller.SignalController import SignalControler
from Models.Asset.Asset import Asset
from Models.Strategy.TestStrategy import TestStrategy
from Services.TradingService import TradingService
from TechnicalModels.BrokerModels.TestBroker import TestBroker
from TechnicalModels.DBModels.MongoDB import DBService
from TechnicalModels.Mapper.DataMapper import DataMapper
from Monitoring.Monitoring import Monitoring
from Services.Helper.SecretsManager import SecretsManager
from Services.RiskManager import RiskManager

# Asset
btc = Asset("BTCUSDT.P", "FVG", "USDT")

# Mapper
dataMapper = DataMapper()

# Broker
tstBroker = TestBroker("Bybit")

# Strategy
fvg = TestStrategy("FVG")

# Monitoring

monitoring = Monitoring()

# Helper

secretsManager = SecretsManager()

secretsMongo = secretsManager.get_secret("mongodb")

# Services

mongoDBData = DBService("TradingData", secretsMongo)
mongoDBTrades = DBService("Trades", secretsMongo)

riskManager = RiskManager(2, 1)

tradingService = TradingService(monitoring, mongoDBData, mongoDBTrades, dataMapper)

# Controller

signalController = SignalControler(monitoring, tradingService)

# Logic

tradingService.createAsset(btc.name, fvg.name, "USDT")
tradingService.addTimeframeToAsset("BTCUSDT.P", "5M")
#tradingService.findOpenTrades()
