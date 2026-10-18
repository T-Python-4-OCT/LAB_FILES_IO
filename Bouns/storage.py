import json


def load_data():
    try:
        with open("studio_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        data = {
            "equipment": [],
            "transactions": []
        }
        save_data(data)

    return data

def save_data(data):
    with open("studio_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)