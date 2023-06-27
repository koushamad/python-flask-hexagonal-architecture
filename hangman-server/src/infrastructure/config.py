# src/infrastructure/config.py

import os
import json


class Config:
    def __init__(self):
        self.WORDS = ["3dhubs", "marvin", "print", "filament", "order", "layer"]
        self.GUESS_LIMIT = 5
        self.config_file_path = "config.json"

    def load_config(self):
        if os.path.exists(self.config_file_path):
            with open(self.config_file_path, "r") as f:
                config_data = json.load(f)
                self.WORDS = config_data.get("WORDS", self.WORDS)
                self.GUESS_LIMIT = config_data.get("GUESS_LIMIT", self.GUESS_LIMIT)
        else:
            self.save_config()

    def save_config(self):
        config_data = {"WORDS": self.WORDS, "GUESS_LIMIT": self.GUESS_LIMIT}
        with open(self.config_file_path, "w") as f:
            json.dump(config_data, f, indent=4)

    def get_words(self):
        return self.WORDS

    def get_guess_limit(self):
        return self.GUESS_LIMIT


config = Config()
config.load_config()
