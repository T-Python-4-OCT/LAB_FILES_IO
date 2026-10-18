
import json
import os
from datetime import date

FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "studio_data.json")

# 1. Load and save data
def load_data():
    if not os.path.exists(FILE_NAME):
        data = {"equipment": [], "transactions": []}
        save_data(data)
        return data

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# 2. Add equipment
def add_equipment(data):
    name = input("Equipment name: ").strip()
    category = input("Category: ").strip()

    try:
        quantity = int(input("Total quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    equipment_id = max(
        [item["id"] for item in data["equipment"]],
        default=0
    ) + 1

    equipment = {
        "id": equipment_id,
        "name": name,
        "category": category,
        "quantity": quantity
    }

    if not name or not category:
        print("Name and category cannot be empty.")
        return

    data["equipment"].append(equipment)
    save_data(data)
    print(f"Equipment added. ID: {equipment_id}")


# 3. View all equipment
def view_equipment(data):
    if not data["equipment"]:
        print("No equipment found.")
        return

    for item in data["equipment"]:
        borrowed = sum(
            transaction["quantity"]
            for transaction in data["transactions"]
            if transaction["equipment_id"] == item["id"]
            and transaction["status"] == "borrowed"
        )

        available = item["quantity"] - borrowed

        print(f"\nID: {item['id']}")
        print(f"Name: {item['name']}")
        print(f"Category: {item['category']}")
        print(f"Total: {item['quantity']}")
        print(f"Borrowed: {borrowed}")
        print(f"Available: {available}")


# 4. Search equipment
def search_equipment(data):
    keyword = input("Enter equipment name or category: ").strip().lower()

    found = False

    for item in data["equipment"]:
        if (keyword in item["name"].lower()
                or keyword in item["category"].lower()):
            print(item)
            found = True

    if not found:
        print("No matching equipment found.")


# 5. Update equipment
def update_equipment(data):
    try:
        equipment_id = int(input("Equipment ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    for item in data["equipment"]:
        if item["id"] == equipment_id:
            name = input("New name (Enter to keep current): ").strip()
            category = input("New category (Enter to keep current): ").strip()
            quantity_text = input("New total quantity (Enter to keep current): ").strip()

            borrowed = sum(
                t["quantity"] for t in data["transactions"]
                if t["equipment_id"] == equipment_id
                and t["status"] == "borrowed"
            )

            if quantity_text:
                try:
                    quantity = int(quantity_text)
                    if quantity < borrowed or quantity <= 0:
                        print("Quantity cannot be less than borrowed units.")
                        return
                    item["quantity"] = quantity
                except ValueError:
                    print("Invalid quantity.")
                    return

            if name:
                item["name"] = name

            if category:
                item["category"] = category

            save_data(data)
            print("Equipment updated.")
            return

    print("Equipment not found.")


# 6. Delete equipment
def delete_equipment(data):
    try:
        equipment_id = int(input("Equipment ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    for item in data["equipment"]:
        if item["id"] == equipment_id:
            borrowed = sum(
                t["quantity"] for t in data["transactions"]
                if t["equipment_id"] == equipment_id
                and t["status"] == "borrowed"
            )

            if borrowed > 0:
                print("Cannot delete equipment that is borrowed.")
                return

            data["equipment"].remove(item)
            save_data(data)
            print("Equipment deleted.")
            return

    print("Equipment not found.")


# 7. Borrow equipment
def borrow_equipment(data):
    employee = input("Employee name: ").strip()

    try:
        equipment_id = int(input("Equipment ID: "))
        quantity = int(input("Quantity to borrow: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if not employee or quantity <= 0:
        print("Invalid employee name or quantity.")
        return

    for item in data["equipment"]:
        if item["id"] == equipment_id:
            borrowed = sum(
                t["quantity"] for t in data["transactions"]
                if t["equipment_id"] == equipment_id
                and t["status"] == "borrowed"
            )

            available = item["quantity"] - borrowed

            if quantity > available:
                print(f"Only {available} units available.")
                return

            transaction_id = max(
                [t["id"] for t in data["transactions"]],
                default=0
            ) + 1

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
            print(f"Borrowing successful. Transaction ID: {transaction_id}")
            return

    print("Equipment not found.")


# 8. Return equipment
def return_equipment(data):
    try:
        transaction_id = int(input("Borrowing transaction ID: "))
    except ValueError:
        print("Invalid transaction ID.")
        return

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


# 9. View borrowing history
def view_borrowing_history(data):
    if not data["transactions"]:
        print("No borrowing history found.")
        return

    for transaction in data["transactions"]:
        print(f"\nTransaction ID: {transaction['id']}")
        print(f"Employee: {transaction['employee']}")
        print(f"Equipment ID: {transaction['equipment_id']}")
        print(f"Quantity: {transaction['quantity']}")
        print(f"Date: {transaction['date']}")
        print(f"Status: {transaction['status']}")
