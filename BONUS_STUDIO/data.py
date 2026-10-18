# ==================================================
# ABDULRAHMAN STUDIO MANAGER 🎬
# Data Management   📦
# ==================================================

import json
import os


FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    "studio_data.json"
)


def load_data():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        data = {
            "equipment": [],
            "transactions": []
        }

        save_data(data)
        return data


def save_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)