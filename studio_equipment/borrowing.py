
from datetime import date
from storage import save_data
from equipment import get_borrowed_quantity


def borrow_equipment(data):
    """Borrow available equipment."""
    employee = input("Enter employee name: ")

    try:
        equipment_id = int(input("Enter equipment ID: "))
        quantity = int(input("Enter quantity to borrow: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    selected_equipment = None

    for item in data["equipment"]:
        if item["id"] == equipment_id:
            selected_equipment = item
            break

    if selected_equipment is None:
        print("Equipment not found.")
        return

    borrowed = get_borrowed_quantity(data, equipment_id)
    available = selected_equipment["quantity"] - borrowed

    if quantity > available:
        print("Not enough equipment available.")
        print("Available quantity:", available)
        return

    transaction_id = 1

    for transaction in data["transactions"]:
        if transaction["id"] >= transaction_id:
            transaction_id = transaction["id"] + 1

    transaction = {
        "id": transaction_id,
        "equipment_id": equipment_id,
        "employee": employee,
        "quantity": quantity,
        "date": str(date.today()),
        "status": "borrowed"
    }

    data["transactions"].append(transaction)
    save_data(data)

    print("Equipment borrowed successfully.")
    print("Transaction ID:", transaction_id)


def return_equipment(data):
    """Return borrowed equipment."""
    try:
        transaction_id = int(input("Enter transaction ID: "))
    except ValueError:
        print("Invalid transaction ID.")
        return

    for transaction in data["transactions"]:
        if transaction["id"] == transaction_id:
            if transaction["status"] == "returned":
                print("This equipment has already been returned.")
                return

            transaction["status"] = "returned"
            save_data(data)

            print("Equipment returned successfully.")
            return

    print("Transaction not found.")


def view_borrowing_history(data):
    """Display all borrowing transactions."""
    if len(data["transactions"]) == 0:
        print("No borrowing history found.")
        return

    for transaction in data["transactions"]:
        equipment_name = "Deleted equipment"

        for item in data["equipment"]:
            if item["id"] == transaction["equipment_id"]:
                equipment_name = item["name"]
                break

        print("\nTransaction ID:", transaction["id"])
        print("Equipment:", equipment_name)
        print("Equipment ID:", transaction["equipment_id"])
        print("Employee:", transaction["employee"])
        print("Quantity:", transaction["quantity"])
        print("Date:", transaction["date"])
        print("Status:", transaction["status"])
