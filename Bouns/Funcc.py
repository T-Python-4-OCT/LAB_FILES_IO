
import json
from datetime import datetime


def load_data():
    try:
        with open("studio_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("Invalid data format")

        if not isinstance(data.get("equipment"), list):
            raise ValueError("Invalid equipment data")

        if not isinstance(data.get("transactions"), list):
            raise ValueError("Invalid transaction data")

        return data

    except FileNotFoundError:
        data = {
            "equipment": [],
            "transactions": []
        }
        save_data(data)
        return data

    except (json.JSONDecodeError, ValueError) as error:
        print("Error loading data:", error)
        raise SystemExit(
            "Please fix studio_data.json before continuing."
        )


def save_data(data):
    with open("studio_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def add_equipment(data):
    name = input("Enter Equipment name: ").strip()
    category = input("Enter Equipment category: ").strip()

    if not name or not category:
        print("Name and category cannot be empty!")
        return

    try:
        quantity = int(input("Enter Quantity: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero!")
        return

    if data["equipment"]:
        new_id = max(item["id"] for item in data["equipment"]) + 1
    else:
        new_id = 1

    equipment = {
        "id": new_id,
        "name": name,
        "category": category,
        "quantity": quantity
    }

    data["equipment"].append(equipment)
    save_data(data)

    print("Equipment added successfully!")
    print("Equipment ID:", new_id)


def view_equipment(data):
    if not data["equipment"]:
        print("The equipment list is empty.")
        return

    for item in data["equipment"]:
        borrowed = 0

        for transaction in data["transactions"]:
            if (transaction["equipment_id"] == item["id"]
                    and transaction["status"] == "borrowed"):
                borrowed += transaction["quantity"]

        available = item["quantity"] - borrowed

        print("-------------------------")
        print("ID:", item["id"])
        print("Name:", item["name"])
        print("Category:", item["category"])
        print("Total:", item["quantity"])
        print("Borrowed:", borrowed)
        print("Available:", available)


def search_equipment(data):
    search = input(
        "Enter name of equipment or category: "
    ).strip().lower()

    if not search:
        print("Please enter a search term!")
        return

    found = False

    for item in data["equipment"]:
        if (search in item["name"].lower()
                or search in item["category"].lower()):

            borrowed = 0

            for transaction in data["transactions"]:
                if (transaction["equipment_id"] == item["id"]
                        and transaction["status"] == "borrowed"):
                    borrowed += transaction["quantity"]

            available = item["quantity"] - borrowed

            print("-------------------------")
            print("ID:", item["id"])
            print("Name:", item["name"])
            print("Category:", item["category"])
            print("Quantity:", item["quantity"])
            print("Available:", available)

            found = True

    if not found:
        print("No matching equipment found!")


def update_equipment(data):
    try:
        equipment_id = int(
            input("Enter equipment Id to update: ")
        )
    except ValueError:
        print("Please enter a valid equipment ID!")
        return

    for item in data["equipment"]:
        if item["id"] == equipment_id:
            print("Equipment found!")
            print("Name:", item["name"])
            print("Category:", item["category"])
            print("Quantity:", item["quantity"])

            new_name = input(
                "Enter new name (Enter to keep current): "
            ).strip()

            new_category = input(
                "Enter new category (Enter to keep current): "
            ).strip()

            new_quantity_input = input(
                "Enter new quantity (Enter to keep current): "
            ).strip()

            if new_name:
                item["name"] = new_name

            if new_category:
                item["category"] = new_category

            borrowed = 0

            for transaction in data["transactions"]:
                if (transaction["equipment_id"] == item["id"]
                        and transaction["status"] == "borrowed"):
                    borrowed += transaction["quantity"]

            if new_quantity_input:
                try:
                    new_quantity = int(new_quantity_input)
                except ValueError:
                    print("Please enter a valid quantity!")
                    return

                if new_quantity <= 0:
                    print("Quantity must be greater than zero!")
                    return

                if new_quantity < borrowed:
                    print(
                        "Quantity cannot be less than "
                        "the amount currently borrowed!"
                    )
                    return

                item["quantity"] = new_quantity

            save_data(data)
            print("Equipment updated successfully!")
            return

    print("Equipment not found!")


def delete_equipment(data):
    try:
        equipment_id = int(
            input("Enter equipment ID to delete: ")
        )
    except ValueError:
        print("Please enter a valid equipment ID!")
        return

    for item in data["equipment"]:
        if item["id"] == equipment_id:
            borrowed = 0

            for transaction in data["transactions"]:
                if (transaction["equipment_id"] == item["id"]
                        and transaction["status"] == "borrowed"):
                    borrowed += transaction["quantity"]

            if borrowed > 0:
                print(
                    "Cannot delete equipment while "
                    "it is borrowed!"
                )
                return

            data["equipment"].remove(item)
            save_data(data)

            print("Equipment deleted successfully!")
            return

    print("Equipment not found!")


def borrow_equipment(data):
    try:
        equipment_id = int(input("Enter equipment ID: "))
    except ValueError:
        print("Please enter a valid equipment ID!")
        return

    for item in data["equipment"]:
        if item["id"] == equipment_id:
            break
    else:
        print("Equipment not found!")
        return

    borrowed = 0

    for transaction in data["transactions"]:
        if (transaction["equipment_id"] == equipment_id
                and transaction["status"] == "borrowed"):
            borrowed += transaction["quantity"]

    available = item["quantity"] - borrowed

    print("Equipment:", item["name"])
    print("Available quantity:", available)

    employee = input("Enter employee name: ").strip()

    if not employee:
        print("Employee name cannot be empty!")
        return

    try:
        quantity = int(input("Enter quantity to borrow: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero!")
        return

    if quantity > available:
        print("Not enough equipment available!")
        return

    if data["transactions"]:
        transaction_id = max(
            transaction["id"] for transaction in data["transactions"]
        ) + 1
    else:
        transaction_id = 1

    transaction = {
        "id": transaction_id,
        "equipment_id": equipment_id,
        "employee": employee,
        "quantity": quantity,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "status": "borrowed"
    }

    data["transactions"].append(transaction)
    save_data(data)

    print("Equipment borrowed successfully!")
    print("Transaction ID:", transaction_id)


def return_equipment(data):
    try:
        transaction_id = int(
            input("Enter transaction ID to return: ")
        )
    except ValueError:
        print("Please enter a valid transaction ID!")
        return

    for transaction in data["transactions"]:
        if transaction["id"] == transaction_id:
            if transaction["status"] == "returned":
                print("This equipment has already been returned!")
                return

            transaction["status"] = "returned"
            save_data(data)

            print("Equipment returned successfully!")
            return

    print("Transaction not found!")


def view_borrowing_history(data):
    if not data["transactions"]:
        print("No borrowing history found!")
        return

    for transaction in data["transactions"]:
        print("-------------------------")
        print("Transaction ID:", transaction["id"])
        print("Equipment ID:", transaction["equipment_id"])
        print("Employee:", transaction["employee"])
        print("Quantity:", transaction["quantity"])
        print("Date:", transaction["date"])
        print("Status:", transaction["status"])
