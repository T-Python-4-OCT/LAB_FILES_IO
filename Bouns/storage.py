import json
import os

FILE_NAME = "studio_data.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        data = {
            "equipment": [],
            "transactions": []
        }

        save_data(data)
        return data

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)