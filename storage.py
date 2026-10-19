import json
import os

FILENAME = "studio_data.json"


def load_data():
    if not os.path.exists(FILENAME):
        data = {"equipment": [], "transactions": []}
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return data
    else:
        with open(FILENAME, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data


def save_data(data):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)