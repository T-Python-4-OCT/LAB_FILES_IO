import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "studio_data.json")


def empty_data():
    return {
        "equipment": [],
        "transactions": [],
        "next_equipment_id": 1,
        "next_transaction_id": 1,
    }


def save_data(data):
    temp_file = DATA_FILE + ".tmp"
    with open(temp_file, "w") as file:
        json.dump(data, file, indent=2)
    os.replace(temp_file, DATA_FILE)


def load_data():
    if not os.path.exists(DATA_FILE):
        data = empty_data()
        save_data(data)
        return data

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        print(f"ERROR: {DATA_FILE} could not be read as valid JSON.")
        print("The file was left untouched. Fix or move it, then start the program again.")
        raise SystemExit(1)

    if (not isinstance(data, dict)
            or not isinstance(data.get("equipment"), list)
            or not isinstance(data.get("transactions"), list)):
        print(f"ERROR: {DATA_FILE} does not have the expected structure.")
        print("The file was left untouched. Fix or move it, then start the program again.")
        raise SystemExit(1)

    if "next_equipment_id" not in data:
        data["next_equipment_id"] = max([e["id"] for e in data["equipment"]], default=0) + 1
    if "next_transaction_id" not in data:
        data["next_transaction_id"] = max([t["id"] for t in data["transactions"]], default=0) + 1
    return data