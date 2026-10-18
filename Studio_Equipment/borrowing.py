"""Borrow, return, and history."""
from datetime import date

from helpers import (read_int, read_text, find_equipment,
                     find_transaction, available_units)
from storage import save_data


def borrow_equipment(data):
    employee = read_text("Employee name: ")
    item = find_equipment(data, read_int("Equipment ID: "))
    if item is None:
        print("Equipment not found.")
        return
    quantity = read_int("Quantity to borrow: ", minimum=1)
    available = available_units(data, item)
    if quantity > available:
        print(f"Rejected: only {available} unit(s) of '{item['name']}' available.")
        return
    t_id = data["counters"]["transaction"]
    data["counters"]["transaction"] += 1
    data["transactions"].append({
        "id": t_id,
        "equipment_id": item["id"],
        "equipment_name": item["name"],  # snapshot, so history survives deletion
        "employee": employee,
        "quantity": quantity,
        "date": date.today().isoformat(),
        "status": "borrowed",
    })
    save_data(data)
    print(f"Borrowed successfully. Transaction ID: {t_id}")


def return_equipment(data):
    t = find_transaction(data, read_int("Transaction ID: "))
    if t is None:
        print("Transaction not found.")
        return
    if t["status"] == "returned":
        print("This transaction was already returned. Nothing changed.")
        return
    t["status"] = "returned"  # availability is calculated, so it recovers by itself
    save_data(data)
    print(f"Transaction {t['id']} returned. {t['quantity']} unit(s) available again.")


def view_history(data):
    if not data["transactions"]:
        print("No transactions yet.")
        return
    for t in data["transactions"]:
        item = find_equipment(data, t["equipment_id"])
        name = item["name"] if item else t.get("equipment_name", "(deleted)")
        print(f"#{t['id']} | {t['date']} | {t['employee']} | "
              f"{name} (ID {t['equipment_id']}) x{t['quantity']} | {t['status']}")