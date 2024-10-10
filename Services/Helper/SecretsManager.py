import os
import json
from configparser import ConfigParser


class SecretsManager:
    def __init__(self, config_file='C:\\Users\\Schule\\FIAE_LS5\\src\\PrintingMachineGit\\Config\\config.ini'):
        self.config_file = config_file
        self.secrets_file_path = self.load_secrets_path()
        # print(f"Pfad zur Secrets-Datei: {self.secrets_file_path}")  # Debug-Ausgabe
        self.secrets = self.load_secrets()

    def load_secrets_path(self):
        """Lade den Pfad zur Secrets-Datei aus der Konfigurationsdatei."""
        config = ConfigParser()
        config.read(self.config_file)
        secrets_path = config.get('paths', 'secrets_path', fallback='Config/secrets.json')
        # print(f"Gelegter secrets_path: {secrets_path}")  # Debug-Ausgabe
        return os.path.join(os.path.dirname(self.config_file), secrets_path)

    def load_secrets(self):
        """Lade die Secrets-Datei und gebe den Inhalt zurück."""
        if not os.path.exists(self.secrets_file_path):
            raise FileNotFoundError(f"Die Datei {self.secrets_file_path} wurde nicht gefunden.")
        with open(self.secrets_file_path, 'r') as f:
            secrets = json.load(f)
        return secrets

    def get_secret(self, key):
        """Gibt das Secret für den angegebenen Schlüssel zurück."""
        return self.secrets.get(key)
