import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "studio_data.json")


def blank_data():
    return {"next_equipment_id": 1, "next_transaction_id": 1, "equipment": [], "transactions": []}


def read_data():
    if not os.path.exists(DATA_FILE):
        data = blank_data()
        write_data(data)
        return data
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        raise SystemExit("Data file is damaged.")
    for key, value in blank_data().items():
        data.setdefault(key, value)
    data["next_equipment_id"] = max([data["next_equipment_id"]] + [i["id"] + 1 for i in data["equipment"]])
    data["next_transaction_id"] = max([data["next_transaction_id"]] + [t["id"] + 1 for t in data["transactions"]])
    return data


def write_data(data):
    temp = DATA_FILE + ".tmp"
    with open(temp, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    os.replace(temp, DATA_FILE)