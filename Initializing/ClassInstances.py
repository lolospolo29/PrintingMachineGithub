from Controller.SignalController import SignalControler
from Models.Asset.Asset import Asset
from Models.Strategy.FVGSession import FVGSession
from Services.Manager.AssetManager import AssetManager
from Services.Manager.StrategyManager import StrategyManager
from Services.Manager.TradeManager import TradeManager
from Services.TradingService import TradingService
from TechnicalModels.BrokerModels.Bybit import Bybit
from TechnicalModels.DBModels.MongoDB import DBService
from TechnicalModels.Mapper.DataMapper import DataMapper
from Monitoring.Monitoring import Monitoring
from Services.Helper.SecretsManager import SecretsManager
from Services.Manager.RiskManager import RiskManager


# Broker
bybit = Bybit("Bybit")

# Strategy
fvgSession = FVGSession("FVGSession")

# Asset
btc = Asset("BTCUSDT.P", fvgSession.name)

btc.addSMTPairName("USDT")
btc.addNewBroker(bybit.name)
btc.addNewTimeFrame("5M")

# Mapper
dataMapper = DataMapper()

# Monitoring

monitoring = Monitoring()

# Helper

secretsManager = SecretsManager()

secretsMongo = secretsManager.get_secret("mongodb")

## Services

# DB
mongoDBData = DBService("TradingData", secretsMongo)
mongoDBTrades = DBService("Trades", secretsMongo)

# Manager / Services
strategyManager = StrategyManager()

assetManager = AssetManager()

riskManager = RiskManager(2, 1)

tradeManager = TradeManager(assetManager, strategyManager, mongoDBTrades, monitoring, dataMapper)

tradingService = TradingService(monitoring, mongoDBData, dataMapper, assetManager,
                                tradeManager)

# Controller

signalController = SignalControler(monitoring, tradingService)

# Logic

assetManager.addAsset(btc)
# tradingService.findOpenTrades()
