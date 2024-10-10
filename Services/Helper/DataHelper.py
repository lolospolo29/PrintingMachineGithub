import json
import os
import random
import time


class DataHelper:

    # for MongoDB
    def ConvertClassToDict(self, obj):
        if isinstance(obj, list):
            return [self.ConvertClassToDict(item) for item in obj]
        elif hasattr(obj, "__dict__"):
            return {key: self.ConvertClassToDict(value) for key, value in obj.__dict__.items()}
        else:
            return obj

    # if needed
    def ConvertClassToJson(self, obj):
        """
        Converts an object to a JSON string.
        """
        return json.dumps(self.ConvertClassToDict(obj), indent=4)

    @staticmethod
    def JsonToFileToSafeToFolder(json_data, secrets_manager):
        """Speichert JSON-Daten direkt in eine Datei, benannt nach dem Ticker mit Zeitstempel."""
        # Lade den Pfad aus der SecretsManager-Instanz
        data_path = secrets_manager.get_secret('data_path')

        # JSON-Daten in ein Python-Dictionary umwandeln
        data = json.loads(json_data)

        # Zugriff auf den "tradingViewData"-Teil des Dictionaries
        trading_view_data = data['tradingViewData']

        # Extrahiere relevante Informationen
        ticker = trading_view_data['ticker']
        broker = trading_view_data['broker']
        strategy_name = trading_view_data['strategy']['name']

        # Erzeuge den Dateinamen mit dem Tag, der Uhrzeit und einer 6-stelligen eindeutigen ID
        current_time = time.localtime()
        day = current_time.tm_mday
        hour_minute = time.strftime("%H%M")
        unique_id = random.randint(100000, 999999)  # Zufällige 6-stellige ID
        filename_suffix = f"{day}_{hour_minute}_{unique_id}"

        # Erstelle den Pfad für die JSON-Datei
        broker_dir = os.path.join(data_path, broker.lower())
        strategy_dir = os.path.join(broker_dir, strategy_name.lower())
        ticker_dir = os.path.join(strategy_dir, ticker.lower())
        json_file_path = os.path.join(ticker_dir, f'{ticker}_{filename_suffix}.json')

        # Erstelle den Pfad für die JSON-Datei
        broker_dir = os.path.join(data_path, broker.lower())
        strategy_dir = os.path.join(broker_dir, strategy_name.lower())
        ticker_dir = os.path.join(strategy_dir, ticker.lower())
        json_file_path = os.path.join(ticker_dir, f'{ticker}_{filename_suffix}.json')

        # Erstelle die Ordnerstruktur, falls sie nicht existiert
        os.makedirs(ticker_dir, exist_ok=True)

        # Schreibe die JSON-Daten in die Datei
        with open(json_file_path, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)  # Schöne Ausgabe mit Einrückungen
