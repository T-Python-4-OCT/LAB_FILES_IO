import json
import os
import tempfile
from pathlib import Path


DATA_FILE = Path(__file__).with_name("studio_data.json")


def save_data(data):
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="UTF-8",
            dir=DATA_FILE.parent,
            delete=False,
        ) as file:
            temporary_path = Path(file.name)
            json.dump(data, file, indent=2)
            file.write("\n")

        os.replace(temporary_path, DATA_FILE)
    except OSError:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()
        raise


def load_data():
    if not DATA_FILE.exists():
        data = {
            "equipment": [],
            "transactions": [],
            "next_equipment_id": 1,
        }
        save_data(data)
        return data

    try:
        with DATA_FILE.open("r", encoding="UTF-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"{DATA_FILE.name} contains invalid JSON; existing data was not changed."
        ) from error

    if not isinstance(data, dict):
        raise ValueError(f"{DATA_FILE.name} must contain a JSON object.")
    if not isinstance(data.get("equipment"), list):
        raise ValueError(f'{DATA_FILE.name} must contain an "equipment" list.')
    if not isinstance(data.get("transactions"), list):
        raise ValueError(f'{DATA_FILE.name} must contain a "transactions" list.')
    if "next_equipment_id" not in data:
        previous_ids = [item["id"] for item in data["equipment"]]
        previous_ids.extend(
            transaction["equipment_id"] for transaction in data["transactions"]
        )
        data["next_equipment_id"] = max(previous_ids, default=0) + 1

    return data


def get_equipment_by_id(data, equipment_id):
    return next(
        (item for item in data["equipment"] if item["id"] == equipment_id),
        None,
    )


def get_borrowed_quantity(data, equipment_id):
    return sum(
        transaction["quantity"]
        for transaction in data["transactions"]
        if transaction["equipment_id"] == equipment_id
        and transaction["status"] == "borrowed"
    )


def get_available_quantity(data, equipment):
    return equipment["quantity"] - get_borrowed_quantity(data, equipment["id"])