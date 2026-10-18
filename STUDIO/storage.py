import json
import os
import sys

FILE = "studio_data.json"


def save(data):
    # write to a temp file, then swap it in, so a crash never leaves a half-written file
    with open(FILE + ".tmp", "w") as f:
        json.dump(data, f, indent=2)
    os.replace(FILE + ".tmp", FILE)


def load():
    if not os.path.exists(FILE):
        save({"equipment": [], "transactions": [], "next_eid": 1, "next_tid": 1})
    try:
        with open(FILE) as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        sys.exit(f"{FILE} is damaged. It was NOT changed. Fix it, then restart.")
    # also accept a file that only has "equipment" and "transactions": build the ID counters from it
    data.setdefault("equipment", [])
    data.setdefault("transactions", [])
    data.setdefault("next_eid", max([e["id"] for e in data["equipment"]], default=0) + 1)
    data.setdefault("next_tid", max([t["id"] for t in data["transactions"]], default=0) + 1)
    return data

#MohammedAlnsafi