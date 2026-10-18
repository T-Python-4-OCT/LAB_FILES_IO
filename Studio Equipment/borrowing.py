from datetime import date

from storage import save_data
from helpers import (read_positive_int, read_text, find_equipment,
                     find_transaction, available_count)


def borrow_equipment(data):
    employee = read_text("Employee name: ")
    if employee is None:
        return
    equipment_id = read_positive_int("Equipment ID: ")
    if equipment_id is None:
        return
    item = find_equipment(data, equipment_id)
    if item is None:
        print(f"No equipment with ID {equipment_id}.")
        return
    quantity = read_positive_int("Quantity to borrow: ")
    if quantity is None:
        return

    available = available_count(data, item)
    if quantity > available:
        print(f"Rejected: only {available} unit(s) of '{item['name']}' are available.")
        return

    transaction = {
        "id": data["next_transaction_id"],
        "equipment_id": equipment_id,
        "equipment_name": item["name"],
        "employee": employee,
        "quantity": quantity,
        "date": date.today().isoformat(),
        "status": "borrowed",
    }
    data["transactions"].append(transaction)
    data["next_transaction_id"] += 1
    save_data(data)
    print(f"Borrowed. Transaction ID: {transaction['id']}. "
          f"Available now: {available - quantity}.")


def return_equipment(data):
    transaction_id = read_positive_int("Borrowing transaction ID: ")
    if transaction_id is None:
        return
    transaction = find_transaction(data, transaction_id)
    if transaction is None:
        print(f"No transaction with ID {transaction_id}.")
        return
    if transaction["status"] == "returned":
        print(f"Transaction {transaction_id} was already returned. Nothing was changed.")
        return

    transaction["status"] = "returned"
    transaction["return_date"] = date.today().isoformat()
    save_data(data)
    print(f"Returned. {transaction['quantity']} unit(s) of "
          f"'{transaction['equipment_name']}' are available again.")


def view_history(data):
    if not data["transactions"]:
        print("There are no borrowing transactions yet.")
        return
    for transaction in data["transactions"]:
        item = find_equipment(data, transaction["equipment_id"])
        if item is not None:
            name = item["name"]
        else:
            name = transaction["equipment_name"] + " (deleted)"
        line = (f"Transaction {transaction['id']} | {transaction['employee']} | {name} "
                f"(ID {transaction['equipment_id']}) | Qty: {transaction['quantity']} | "
                f"Borrowed: {transaction['date']} | {transaction['status']}")
        if transaction["status"] == "returned":
            line += f" on {transaction['return_date']}"
        print(line)