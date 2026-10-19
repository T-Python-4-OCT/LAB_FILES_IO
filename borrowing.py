
from datetime import date
from storage import save_data
from equipment import get_equipment, get_borrowed_quantity


def borrow_equipment(data):
    employee = input("Enter employee name: ").strip()

    if not employee:
        print("Employee name cannot be empty")
        return

    try:
        equipment_id = int(input("Enter equipment ID: "))
        quantity = int(input("Enter quantity to borrow: "))
    except ValueError:
        print("Invalid ID or quantity")
        return

    item = get_equipment(data, equipment_id)

    if item is None:
        print("Equipment not found")
        return

    available = item["quantity"] - get_borrowed_quantity(data, equipment_id)

    if quantity <= 0:
        print("Quantity must be greater than zero")
        return

    if quantity > available:
        print("Not enough equipment available")
        print("Available:", available)
        return

    transaction_id = max(
        [t["id"] for t in data["transactions"]],
        default=0
    ) + 1

    data["transactions"].append({
        "id": transaction_id,
        "equipment_id": equipment_id,
        "employee": employee,
        "quantity": quantity,
        "date": str(date.today()),
        "status": "borrowed"
    })

    save_data(data)
    print("Equipment borrowed successfully")
    print("Transaction ID:", transaction_id)


def return_equipment(data):
    try:
        transaction_id = int(input("Enter transaction ID: "))
    except ValueError:
        print("Invalid transaction ID")
        return

    for transaction in data["transactions"]:
        if transaction["id"] == transaction_id:

            if transaction["status"] == "returned":
                print("This equipment has already been returned")
                return

            transaction["status"] = "returned"
            save_data(data)

            print("Equipment returned successfully")
            return

    print("Transaction not found")


def view_borrowing_history(data):
    if not data["transactions"]:
        print("No borrowing history found")
        return

    for transaction in data["transactions"]:
        print("*" * 20)
        print("Transaction ID:", transaction["id"])
        print("Employee:", transaction["employee"])
        print("Equipment ID:", transaction["equipment_id"])
        print("Quantity:", transaction["quantity"])
        print("Date:", transaction["date"])
        print("Status:", transaction["status"])
