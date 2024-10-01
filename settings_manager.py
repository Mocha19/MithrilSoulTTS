import json
import os

class SettingsManager:
    def __init__(self, filename='user_data.json'):
        self.filename = filename
        self.data = {}
        self.load_settings()

    # Load settings from the JSON file.
    def load_settings(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                self.data = {}

    # Save settings to the JSON file.
    def save_settings(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)

    # Get a setting value, with a default fallback.
    def get(self, key, default=None):
        return self.data.get(key, default)

    # Set a setting value and save it.
    def set(self, key, value):
        self.data[key] = value
        self.save_settings()
