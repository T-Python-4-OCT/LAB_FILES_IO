import json
import os

FILE_NAME = "studio_data.json"


def load_data():
    #if the file does not exist, create it with an empty structure
    if not os.path.exists(FILE_NAME):
        data = {
            "next_equipment_id": 1,
            "next_transaction_id": 1,
            "equipment": [],
            "transactions": []
        }
        save_data(data)
        return data

    with open(FILE_NAME, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def save_data(data):
    with open(FILE_NAME, "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4)
