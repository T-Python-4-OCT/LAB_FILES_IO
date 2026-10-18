
from studio.storeg import save_data
from studio.equipment import (
    get_equipment,
    get_available_quantity,
    get_positive_integer
)
from datetime import date


def borrow_equipment(data):
    employee = input("Employee name: ").strip()

    if not employee:
        print("Employee name cannot be empty.")
        return

    equipment_id = get_positive_integer("Equipment ID: ")
    item = get_equipment(data, equipment_id)

    if item is None:
        print("Equipment not found.")
        return

    available = get_available_quantity(data, item)
    print("Available quantity:", available)

    quantity = get_positive_integer("Quantity to borrow: ")

    if quantity > available:
        print("Not enough equipment available.")
        return

    transaction = {
        "id": data["next_transaction_id"],
        "equipment_id": equipment_id,
        "employee": employee,
        "quantity": quantity,
        "date": date.today().isoformat(),
        "status": "borrowed"
    }

    data["transactions"].append(transaction)
    data["next_transaction_id"] += 1

    save_data(data)

    print("Borrowing successful.")
    print("Transaction ID:", transaction["id"])
    print("Available now:", get_available_quantity(data, item))


def return_equipment(data):
    transaction_id = get_positive_integer("Transaction ID: ")

    transaction = None

    for record in data["transactions"]:
        if record["id"] == transaction_id:
            transaction = record
            break

    if transaction is None:
        print("Transaction not found.")
        return

    if transaction["status"] == "returned":
        print("This transaction has already been returned.")
        return

    transaction["status"] = "returned"
    save_data(data)

    print("Equipment returned successfully.")

    item = get_equipment(data, transaction["equipment_id"])

    if item is not None:
        print("Available now:", get_available_quantity(data, item))



def view_borrowing_history(data):
    transactions = data.get("transactions", [])

    if not transactions:
        print("No borrowing history found.")
        return

    for transaction in transactions:
        item = get_equipment(data, transaction["equipment_id"])

        if item:
            equipment_name = item["name"]
        else:
            equipment_name = "Deleted equipment"

        print("\n==============================")
        print("Transaction ID:", transaction["id"])
        print("Employee:", transaction["employee"])
        print("Equipment:", equipment_name)
        print("Equipment ID:", transaction["equipment_id"])
        print("Quantity:", transaction["quantity"])
        print("Date:", transaction["date"])
        print("Status:", transaction["status"])
        print("==============================")
