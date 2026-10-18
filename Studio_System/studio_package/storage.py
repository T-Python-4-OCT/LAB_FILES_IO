
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "studio_data.json"


def load_data():
    if not DATA_FILE.exists():
        data = {
            "equipment": [],
            "transactions": []
        }
        save_data(data)
        return data

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
