
import json
import os

FILE_NAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "studio_data.json"
)


def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)

        except (json.JSONDecodeError, OSError) as error:
            raise RuntimeError(
                f"Could not read {FILE_NAME}: {error}"
            ) from error

    return {
        "equipment": [],
        "transactions": [],
        "next_equipment_id": 1,
        "next_transaction_id": 1
    }


def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
