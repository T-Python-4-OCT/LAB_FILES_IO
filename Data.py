import json
import os

DATA_FILE = "studio_data.json"



def empty_data():
    return {
        "equipment": [],
        "transactions": [],
        "next_equipment_id": 1,
        "next_transaction_id": 1,
    }


def save_data(data):
    tmp = DATA_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.replace(tmp, DATA_FILE)


def load_data():
    if not os.path.exists(DATA_FILE):
        data = empty_data()
        save_data(data)
        return data

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        # Do NOT overwrite a damaged file: stop so the user can fix it.
        print(f"ERROR: {DATA_FILE} is unreadable or corrupted.")
        print("The program will not overwrite it. Fix or rename the file and try again.")
        raise SystemExit(1)

    data.setdefault("equipment", [])
    data.setdefault("transactions", [])
    max_eq = max((e["id"] for e in data["equipment"]), default=0)
    max_tx = max((t["id"] for t in data["transactions"]), default=0)
    data["next_equipment_id"] = max(data.get("next_equipment_id", 1), max_eq + 1)
    data["next_transaction_id"] = max(data.get("next_transaction_id", 1), max_tx + 1)
    return data


def find_equipment(data, equipment_id):
    for item in data["equipment"]:
        if item["id"] == equipment_id:
            return item
    return None


def find_transaction(data, transaction_id):
    for tx in data["transactions"]:
        if tx["id"] == transaction_id:
            return tx
    return None


def borrowed_count(data, equipment_id):
   
    return sum(
        tx["quantity"]
        for tx in data["transactions"]
        if tx["equipment_id"] == equipment_id and tx["status"] == "borrowed"
    )


def available_count(data, item):
    return item["quantity"] - borrowed_count(data, item["id"])