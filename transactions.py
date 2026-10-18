#
import json
from datetime import datetime 
def borrow_equipment():
    with open("studio_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    equipment_list = data["equipment"]
    transactions = data["transactions"]

    if not equipment_list:
        print("No equipment available.")
        return

    print("\nAvailable Equipment:")

    for equipment in equipment_list:
        borrowed_quantity = sum(
            int(transaction["quantity"])
            for transaction in transactions
            if transaction["equipment_id"] == equipment["id"]
            and transaction["status"] == "borrowed"
        )

        available_quantity = int(equipment["quantity"]) - borrowed_quantity

        print(
            f"ID: {equipment['id']} | "
            f"Name: {equipment['name']} | "
            f"Available: {available_quantity}"
        )

    try:
        equipment_id = int(input("\nEnter equipment ID: "))
        quantity = int(input("Enter quantity to borrow: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

    except ValueError:
        print("Please enter valid numbers.")
        return

    employee = input("Enter employee name: ").strip()

    if not employee:
        print("Employee name cannot be empty.")
        return

    selected_equipment = None

    for equipment in equipment_list:
        if equipment["id"] == equipment_id:
            selected_equipment = equipment
            break

    if selected_equipment is None:
        print("Equipment ID not found.")
        return

    borrowed_quantity = sum(
        transaction["quantity"]
        for transaction in transactions
        if transaction["equipment_id"] == equipment_id
        and transaction["status"] == "borrowed"
    )

    available_quantity = (
        int(selected_equipment["quantity"]) - borrowed_quantity
    )

    if quantity > available_quantity:
        print(f"Not enough equipment available. Available: {available_quantity}")
        return

    transaction_id = max(
        (transaction["id"] for transaction in transactions),
        default=0
    ) + 1

    new_transaction = {
        "id": transaction_id,
        "equipment_id": equipment_id,
        "employee": employee,
        "quantity": quantity,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "borrowed"
    }

    transactions.append(new_transaction)

    with open("studio_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("Equipment borrowed successfully!")
    print(f"Transaction ID: {transaction_id}")


def return_equipment():
    with open("studio_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    transactions = data["transactions"]

    active_transactions = [
        transaction for transaction in transactions
        if transaction["status"] == "borrowed"
    ]

    if not active_transactions:
        print("No equipment currently borrowed.")
        return

    print("\nActive Borrowing Transactions:")

    for transaction in active_transactions:
        print(
            f"Transaction ID: {transaction['id']} | "
            f"Equipment ID: {transaction['equipment_id']} | "
            f"Employee: {transaction['employee']} | "
            f"Quantity: {transaction['quantity']}"
        )

    try:
        transaction_id = int(
            input("\nEnter transaction ID to return: ")
        )
    except ValueError:
        print("Please enter a valid transaction ID.")
        return

    for transaction in transactions:
        if transaction["id"] == transaction_id:

            if transaction["status"] != "borrowed":
                print("This transaction has already been returned.")
                return

            transaction["status"] = "returned"
            transaction["return_date"] = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            with open("studio_data.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

            print("Equipment returned successfully!")
            return

    print("Transaction ID not found.")


def view_transactions():
    with open("studio_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    transactions = data["transactions"]
    equipment_list = data["equipment"]

    if not transactions:
        print("No transaction history found.")
        return

    print("\n========== Transaction History ==========")

    for transaction in transactions:
        equipment_name = "Unknown Equipment"

        for equipment in equipment_list:
            if equipment["id"] == transaction["equipment_id"]:
                equipment_name = equipment["name"]
                break

        print(f"\nTransaction ID: {transaction['id']}")
        print(f"Equipment: {equipment_name}")
        print(f"Equipment ID: {transaction['equipment_id']}")
        print(f"Employee: {transaction['employee']}")
        print(f"Quantity: {transaction['quantity']}")
        print(f"Borrow Date: {transaction['date']}")
        print(f"Status: {transaction['status']}")

        if "return_date" in transaction:
            print(f"Return Date: {transaction['return_date']}")

        print("-----------------------------------------")
