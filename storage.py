import json
import os

DATA_FILE = "studio_data.json"


def load_data():
  if not os.path.exists(DATA_FILE):
    initial_data = {"equipment": [], "transactions": []}
    save_data(initial_data)
    return initial_data
  with open(DATA_FILE, "r") as file:
    return json.load(file)


def save_data(data):
  with open(DATA_FILE, "w") as file:
    json.dump(data, file, indent=4)