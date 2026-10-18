
from datetime import date

from .storage import save_data
from .equipment import get_available_quantity


def borrow_equipment(data):
    employee = input("Employee name: ").strip()

    if not employee:
        print("Employee name cannot be empty.")
        return

    try:
        equipment_id = int(input("Equipment ID: "))
        quantity = int(input("Quantity to borrow: "))
    except ValueError:
        print("ID and quantity must be valid numbers.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    equipment = next(
        (
            item for item in data["equipment"]
            if item["id"] == equipment_id
        ),
        None
    )

    if equipment is None:
        print("Equipment not found.")
        return

    available = get_available_quantity(data, equipment)

    if quantity > available:
        print(f"Not enough equipment available. Available: {available}")
        return

    transaction_id = max(
        (transaction["id"] for transaction in data["transactions"]),
        default=0
    ) + 1

    transaction = {
        "id": transaction_id,
        "equipment_id": equipment_id,
        "employee": employee,
        "quantity": quantity,
        "date": date.today().isoformat(),
        "status": "borrowed"
    }

    data["transactions"].append(transaction)
    save_data(data)

    print(f"Borrowing successful. Transaction ID: {transaction_id}")


def return_equipment(data):
    try:
        transaction_id = int(input("Borrowing transaction ID: "))
    except ValueError:
        print("Invalid transaction ID.")
        return

    transaction = next(
        (
            item for item in data["transactions"]
            if item["id"] == transaction_id
        ),
        None
    )

    if transaction is None:
        print("Transaction not found.")
        return

    if transaction["status"] == "returned":
        print("This transaction has already been returned.")
        return

    transaction["status"] = "returned"
    save_data(data)

    print("Equipment returned successfully.")


def view_borrowing_history(data):
    if not data["transactions"]:
        print("No borrowing transactions found.")
        return

    print("\n--- Borrowing History ---")

    for transaction in data["transactions"]:
        equipment = next(
            (
                item for item in data["equipment"]
                if item["id"] == transaction["equipment_id"]
            ),
            None
        )

        equipment_name = (
            equipment["name"] if equipment else "Deleted equipment"
        )

        print(f"\nTransaction ID: {transaction['id']}")
        print(f"Employee: {transaction['employee']}")
        print(f"Equipment: {equipment_name}")
        print(f"Equipment ID: {transaction['equipment_id']}")
        print(f"Quantity: {transaction['quantity']}")
        print(f"Date: {transaction['date']}")
        print(f"Status: {transaction['status']}")
