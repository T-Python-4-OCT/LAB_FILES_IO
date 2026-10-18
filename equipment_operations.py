from datetime import date

from equipment_data import (
    get_available_quantity,
    get_borrowed_quantity,
    get_equipment_by_id,
    save_data,
)


def prompt_integer(message, minimum=None):
    while True:
        try:
            value = int(input(message).strip())
        except ValueError:
            print("Please enter a whole number.")
            continue

        if minimum is not None and value < minimum:
            print(f"Please enter a number greater than or equal to {minimum}.")
            continue
        return value


def add_equipment(data):
    name = input("Enter equipment name: ").strip()
    category = input("Enter equipment category: ").strip()
    if not name or not category:
        print("Name and category cannot be empty.")
        return

    quantity = prompt_integer("Enter total quantity: ", minimum=1)
    equipment_id = data["next_equipment_id"]
    equipment = {
        "id": equipment_id,
        "name": name,
        "category": category,
        "quantity": quantity,
    }
    data["equipment"].append(equipment)
    data["next_equipment_id"] += 1
    save_data(data)
    print(f"Equipment added with ID {equipment_id}.")


def print_equipment(data, equipment):
    borrowed = get_borrowed_quantity(data, equipment["id"])
    available = get_available_quantity(data, equipment)
    print(
        f"ID: {equipment['id']} | {equipment['name']} | {equipment['category']}\n"
        f"Total: {equipment['quantity']} | Borrowed: {borrowed} | Available: {available}"
    )


def view_all_equipment(data):
    if not data["equipment"]:
        print("No equipment found.")
        return

    for equipment in data["equipment"]:
        print_equipment(data, equipment)


def search_equipment(data):
    query = input("Search by equipment name or category: ").strip().casefold()
    if not query:
        print("Search term cannot be empty.")
        return

    matches = [
        item
        for item in data["equipment"]
        if query in item["name"].casefold()
        or query in item["category"].casefold()
    ]
    if not matches:
        print("No matching equipment found.")
        return

    for equipment in matches:
        print_equipment(data, equipment)


def update_equipment(data):
    equipment_id = prompt_integer("Enter equipment ID to update: ", minimum=1)
    equipment = get_equipment_by_id(data, equipment_id)
    if equipment is None:
        print("Equipment not found.")
        return

    print("1. Update name")
    print("2. Update category")
    print("3. Update total quantity")
    choice = input("Select an option: ").strip()

    if choice == "1":
        value = input("Enter the new name: ").strip()
        if not value:
            print("Name cannot be empty.")
            return
        equipment["name"] = value
    elif choice == "2":
        value = input("Enter the new category: ").strip()
        if not value:
            print("Category cannot be empty.")
            return
        equipment["category"] = value
    elif choice == "3":
        borrowed = get_borrowed_quantity(data, equipment_id)
        quantity = prompt_integer(
            f"Enter new total quantity (at least {max(1, borrowed)}): ",
            minimum=max(1, borrowed),
        )
        equipment["quantity"] = quantity
    else:
        print("Invalid option.")
        return

    save_data(data)
    print("Equipment updated.")


def delete_equipment(data):
    equipment_id = prompt_integer("Enter equipment ID to delete: ", minimum=1)
    equipment = get_equipment_by_id(data, equipment_id)
    if equipment is None:
        print("Equipment not found.")
        return

    borrowed = get_borrowed_quantity(data, equipment_id)
    if borrowed:
        print(f"Cannot delete: {borrowed} unit(s) are currently borrowed.")
        return

    data["equipment"].remove(equipment)
    save_data(data)
    print("Equipment deleted.")


def borrow_equipment(data):
    employee = input("Enter employee name: ").strip()
    if not employee:
        print("Employee name cannot be empty.")
        return

    equipment_id = prompt_integer("Enter equipment ID to borrow: ", minimum=1)
    equipment = get_equipment_by_id(data, equipment_id)
    if equipment is None:
        print("Equipment not found.")
        return

    available = get_available_quantity(data, equipment)
    quantity = prompt_integer("Enter quantity to borrow: ", minimum=1)
    if quantity > available:
        print(f"Request rejected. Only {available} unit(s) are available.")
        return

    transaction_id = max(
        (transaction["id"] for transaction in data["transactions"]),
        default=0,
    ) + 1
    data["transactions"].append(
        {
            "id": transaction_id,
            "equipment_id": equipment_id,
            "employee": employee,
            "quantity": quantity,
            "date": date.today().isoformat(),
            "status": "borrowed",
        }
    )
    save_data(data)
    print(f"Borrow successful. Transaction ID: {transaction_id}")


def return_equipment(data):
    transaction_id = prompt_integer("Enter borrowing transaction ID: ", minimum=1)
    transaction = next(
        (item for item in data["transactions"] if item["id"] == transaction_id),
        None,
    )
    if transaction is None:
        print("Transaction not found.")
        return
    if transaction["status"] == "returned":
        print("This transaction has already been returned.")
        return

    transaction["status"] = "returned"
    save_data(data)
    print("Equipment returned.")


def view_borrowing_history(data):
    if not data["transactions"]:
        print("No borrowing history found.")
        return

    for transaction in data["transactions"]:
        equipment = get_equipment_by_id(data, transaction["equipment_id"])
        equipment_name = equipment["name"] if equipment else "Deleted equipment"
        print(
            f"Transaction ID: {transaction['id']} | Employee: {transaction['employee']} | "
            f"Equipment: {equipment_name} (ID: {transaction['equipment_id']}) | "
            f"Quantity: {transaction['quantity']} | Date: {transaction['date']} | "
            f"Status: {transaction['status']}"
        )