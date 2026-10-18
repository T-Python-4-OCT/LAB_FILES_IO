import json
import os

DB_FILE = "studio_data.json"


def load_data():
  if not os.path.exists(DB_FILE):
    initial_data = {"equipment": [], "transactions": []}
    save_data(initial_data)
    return initial_data

  try:
    with open(DB_FILE, "r", encoding="utf-8") as file:
      return json.load(file)
  except (json.JSONDecodeError, FileNotFoundError):
    return {"equipment": [], "transactions": []}


def save_data(data):
  with open(DB_FILE, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)