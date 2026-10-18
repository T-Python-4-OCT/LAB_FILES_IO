
import json


def load_data():
    """Load data from the JSON file."""
    try:
        with open("studio_data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        data = {
            "equipment": [],
            "transactions": []
        }
        save_data(data)

    return data


def save_data(data):
    """Save data to the JSON file."""
    with open("studio_data.json", "w") as file:
        json.dump(data, file, indent=4)
