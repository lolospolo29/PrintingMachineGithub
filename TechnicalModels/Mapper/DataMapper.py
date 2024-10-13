import datetime

import pytz

from Models.Asset.strategyData import strategyData
from Models.Trade.Order import Order
from Models.Trade.Trade import Trade
from Models.TradingData import TradingData


class DataMapper:
    def MapToClass(self, data, name):
        # If _id is present, handle it as needed (e.g., ignore or use it)
        # For this example, we'll just ignore it

        if name == "tradingData":
            data = data.get("tradingData")

            # Handle asset
            asset_value = data.get('asset')
            asset_value = asset_value.strip("'") if asset_value else None  # Remove single quotes from asset

            timeFrame = data.get('timeFrame')
            timeFrame = timeFrame.strip("'") if asset_value else None  # Remove single quotes from asset

            # Handle time
            current_time_utc = datetime.datetime.now(pytz.utc)

            formatted_time = current_time_utc.strftime("%H:%M")

            return TradingData(
                asset=asset_value,
                open=data.get('open'),
                close=data.get('close'),
                high=data.get('high'),
                low=data.get('low'),
                time=formatted_time,  # Use the formatted time
                timeFrame=timeFrame
            )
        if name == "Trade":
            # Mappe die Daten auf das Trade-Objekt
            data = data.get("Trade")

            # Handle asset
            asset_value = data.get('asset')
            asset_value = asset_value.strip("'") if asset_value else None  # Entferne einfache Anführungszeichen

            # Handle strategyName
            strategy_name = data.get('strategyName', '')

            # Initialisiere das Trade-Objekt
            trade = Trade(asset=asset_value, strategyName=strategy_name)

            # Mappe den Status und PnL
            trade.status = data.get('status', None)
            trade.pnl = data.get('pnl', 0)

            # Verarbeite die Order-Liste, falls vorhanden
            orderJSON = data.get('orders')
            for orderData in orderJSON:
                trade.orders.append(self.MapToClass("order", orderData))

            return trade
        if name == "order":
            order = Order()
            order.status = data.get('status')
            order.id = data.get('id')
            order.stopLoss = data.get('stopLoss')
            order.takeProfit = data.get('takeProfit')
            order.riskPercentage = data.get('riskPercentage')
            order.broker = data.get('broker')
            return order
        if name == "strategyData":
            asset_data = data.get("AssetData")
            if not asset_data:
                raise ValueError("AssetData is missing from the input data")

            timeFrame = asset_data.get('timeFrame')
            timeStamp = asset_data.get('timeStamp')

            # Get price and time arrays from the asset data
            open_values = asset_data.get('open', [])
            close_values = asset_data.get('close', [])
            high_values = asset_data.get('high', [])
            low_values = asset_data.get('low', [])
            time_values = asset_data.get('time', [])

            # Create and return strategyData object
            strategy_data = strategyData(
                timeStamp=timeStamp,
                timeFrame=timeFrame
            )

            # Map open, close, high, low, and time values
            strategy_data.open = open_values
            strategy_data.close = close_values
            strategy_data.high = high_values
            strategy_data.low = low_values
            strategy_data.time = time_values

            return strategy_data
