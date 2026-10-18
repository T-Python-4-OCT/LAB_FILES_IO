
import json
import os

FILE_NAME = "studio_data.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        data = {
            "equipment": [],
            "transactions": [],
            "next_equipment_id": 1,
            "next_transaction_id": 1
        }
        save_data(data)
        return data

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        data = json.load(file)

  
    data.setdefault("equipment", [])
    data.setdefault("transactions", [])

    data["next_equipment_id"] = max(
        data.get("next_equipment_id", 1),
        max((item["id"] for item in data["equipment"]), default=0) + 1
    )

    data["next_transaction_id"] = max(
        data.get("next_transaction_id", 1),
        max((item["id"] for item in data["transactions"]), default=0) + 1
    )

    return data


def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
