from datetime import date
from data_file import save_data
from tools import read_number, find_equipment, find_transaction, get_borrowed


def borrow_equipment(data):
    employee = input("Employee name: ")
    if employee == "":
        print("Employee name cannot be empty")
        return
    equipment_id = read_number("Equipment ID: ")
    item = find_equipment(data, equipment_id)
    if item is None:
        print("No equipment with this ID")
        return

    quantity = read_number("Quantity to borrow: ")
    available = item["quantity"] - get_borrowed(data, equipment_id)

    if quantity == 0:
        print("Quantity must be more than 0")
        return
    if quantity > available:
        print("Rejected, only", available, "available")
        return

    transaction = {
        "id": data["next_transaction_id"],
        "equipment_id": equipment_id,
        "employee": employee,
        "quantity": quantity,
        "date": str(date.today()),
        "status": "borrowed"
    }
    data["transactions"].append(transaction)
    data["next_transaction_id"] = data["next_transaction_id"] + 1
    save_data(data)
    print("Borrowed successfully, your transaction ID is", transaction["id"])
    print("Available now:", available - quantity)


def return_equipment(data):
    transaction_id = read_number("Transaction ID: ")
    transaction = find_transaction(data, transaction_id)
    if transaction is None:
        print("No transaction with this ID")
        return

    #returning the same transaction twice is not allowed
    if transaction["status"] == "returned":
        print("This transaction was already returned")
        return

    transaction["status"] = "returned"
    save_data(data)
    print(transaction["employee"], "returned", transaction["quantity"], "units")

    item = find_equipment(data, transaction["equipment_id"])
    if item is not None:
        print("Available now:", item["quantity"] - get_borrowed(data, item["id"]))


def view_history(data):
    if len(data["transactions"]) == 0:
        print("No borrowing history yet")
        return
    for t in data["transactions"]:
        print("Transaction", t["id"], "|", t["date"], "|", t["employee"],
              "| equipment ID", t["equipment_id"], "| quantity", t["quantity"], "|", t["status"])
