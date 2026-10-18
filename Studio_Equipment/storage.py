"""Loading and saving the JSON file."""
import json
import os
import sys

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "studio_data.json")


def empty_data():
    return {"equipment": [], "transactions": [],
            "counters": {"equipment": 1, "transaction": 1}}


def fix_counters(data):
    """Make sure counters exist and are always ahead of any used ID."""
    counters = data.setdefault("counters", {})
    max_e = max([e["id"] for e in data["equipment"]], default=0)
    max_t = max([t["id"] for t in data["transactions"]], default=0)
    counters["equipment"] = max(counters.get("equipment", 1), max_e + 1)
    counters["transaction"] = max(counters.get("transaction", 1), max_t + 1)
    return data


def save_data(data):
    """Atomic save: write a temp file, then replace the real one."""
    tmp = DATA_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp, DATA_FILE)


def load_data():
    if not os.path.exists(DATA_FILE):
        data = empty_data()
        save_data(data)
        return data
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        data.setdefault("equipment", [])
        data.setdefault("transactions", [])
        return fix_counters(data)
    except (json.JSONDecodeError, OSError, KeyError, TypeError) as err:
        # Never overwrite a damaged file: that would erase the records.
        print(f"Error: cannot read {DATA_FILE} ({err}).")
        print("The file was left untouched. Fix or move it, then restart.")
        sys.exit(1)