import asyncio
from threading import Thread

from flask import Flask, request

from Initializing.ClassInstances import signalController

# rom Classes import AlertSignal, TradeSignal

app = Flask(__name__)


@app.route('/tradingview', methods=['POST'])
def receive_signal():
    jsonString = request.get_json()

    thread = Thread(target=signalController.orderSignal(jsonString))
    thread.start()

    return f'Received Analyse data: {jsonString}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# API Secrets
# Name : DemoApiKey
# Api Key : Ifp91Iy8fOY6x22bVG
# Secret: eagubhmZG5nY0gbycEeJNGR50GuT5YnpZA37
