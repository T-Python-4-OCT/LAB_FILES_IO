import json


FILE_NAME = "studio_data.json"


def save_data(data):
    """Save studio data to the JSON file."""

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_data():
    """Load studio data or create the file if it does not exist."""

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        data = {
            "equipment": [],
            "transactions": []
        }

        save_data(data)

        return data