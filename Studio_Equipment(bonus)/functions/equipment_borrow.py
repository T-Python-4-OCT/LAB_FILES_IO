
from datetime import date


def borrow_equipment(data):
    employee = input("Employee name: ").strip()

    if not employee:
        print("Employee name cannot be empty.")
        return False

    try:
        equipment_id = int(input("Equipment ID: "))
        quantity = int(input("Quantity to borrow: "))

    except ValueError:
        print("Please enter valid numbers.")
        return False

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return False

    for equipment in data["equipment"]:
        if equipment["id"] == equipment_id:
            borrowed = 0

            for transaction in data["transactions"]:
                if (transaction["equipment_id"] == equipment_id
                        and transaction["status"] == "borrowed"):
                    borrowed += transaction["quantity"]

            available = equipment["quantity"] - borrowed

            if quantity > available:
                print(f"Only {available} units available.")
                return False

            transaction_id = data["next_transaction_id"]

            transaction = {
                "id": transaction_id,
                "equipment_id": equipment_id,
                "employee": employee,
                "quantity": quantity,
                "date": date.today().isoformat(),
                "status": "borrowed"
            }

            data["transactions"].append(transaction)
            data["next_transaction_id"] += 1

            print("Equipment borrowed successfully!")
            print(f"Transaction ID: {transaction_id}")
            print(f"Remaining available: {available - quantity}")

            return True

    print("Equipment not found.")
    return False


def return_equipment(data):
    try:
        transaction_id = int(input("Transaction ID: "))

    except ValueError:
        print("Invalid transaction ID.")
        return False

    for transaction in data["transactions"]:
        if transaction["id"] == transaction_id:

            if transaction["status"] == "returned":
                print("Equipment already returned.")
                return False

            if transaction["status"] != "borrowed":
                print("Invalid transaction status.")
                return False

            transaction["status"] = "returned"

            print("Equipment returned successfully!")
            print(f"Transaction ID: {transaction_id}")

            return True

    print("Transaction not found.")
    return False


def view_borrowing_history(data):
    if not data["transactions"]:
        print("No borrowing history available.")
        return

    print("\n===== BORROWING HISTORY =====")

    for transaction in data["transactions"]:
        equipment_name = "Unknown"

        for equipment in data["equipment"]:
            if equipment["id"] == transaction["equipment_id"]:
                equipment_name = equipment["name"]
                break

        print(f"\nTransaction ID: {transaction['id']}")
        print(f"Employee: {transaction['employee']}")
        print(f"Equipment ID: {transaction['equipment_id']}")
        print(f"Equipment: {equipment_name}")
        print(f"Quantity: {transaction['quantity']}")
        print(f"Borrow Date: {transaction['date']}")
        print(f"Status: {transaction['status']}")
        print("-" * 30)
