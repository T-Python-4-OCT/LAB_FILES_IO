
from datetime import date

from .storage import save_data
from .equipment import (
    find_equipment,
    available_quantity,
    get_integer
)


def borrow_equipment(data):
    employee = input("Employee name: ").strip()

    if not employee:
        print("Employee name cannot be empty.")
        return

    equipment_id = get_integer("Equipment ID: ")
    item = find_equipment(data, equipment_id)

    if item is None:
        print("Equipment not found.")
        return

    available = available_quantity(data, item)
    print(f"Available quantity: {available}")

    if available == 0:
        print("No units available.")
        return

    quantity = get_integer("Quantity to borrow: ")

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

    print(
        "Borrowing successful. "
        f"Transaction ID: {transaction['id']}"
    )


def return_equipment(data):
    transaction_id = get_integer("Transaction ID: ")

    for transaction in data["transactions"]:
        if transaction["id"] == transaction_id:

            if transaction["status"] == "returned":
                print("This transaction has already been returned.")
                return

            transaction["status"] = "returned"
            save_data(data)

            print("Equipment returned successfully.")
            return

    print("Transaction not found.")


def view_history(data):
    if not data["transactions"]:
        print("No borrowing history found.")
        return

    for transaction in data["transactions"]:
        item = find_equipment(data, transaction["equipment_id"])

        equipment_name = (
            item["name"] if item else "Deleted equipment"
        )

        print("\n-------------------------")
        print(f"Transaction ID: {transaction['id']}")
        print(f"Employee: {transaction['employee']}")
        print(f"Equipment: {equipment_name}")
        print(f"Equipment ID: {transaction['equipment_id']}")
        print(f"Quantity: {transaction['quantity']}")
        print(f"Date: {transaction['date']}")
        print(f"Status: {transaction['status']}")