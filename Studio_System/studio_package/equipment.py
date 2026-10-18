
from .storage import save_data


def get_borrowed_quantity(data, equipment_id):
    return sum(
        transaction["quantity"]
        for transaction in data["transactions"]
        if transaction["equipment_id"] == equipment_id
        and transaction["status"] == "borrowed"
    )


def get_available_quantity(data, equipment):
    borrowed = get_borrowed_quantity(data, equipment["id"])
    return equipment["quantity"] - borrowed


def add_equipment(data):
    name = input("Equipment name: ").strip()
    category = input("Category: ").strip()

    if not name or not category:
        print("Name and category cannot be empty.")
        return

    try:
        quantity = int(input("Total quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    equipment_id = max(
        (item["id"] for item in data["equipment"]),
        default=0
    ) + 1

    equipment = {
        "id": equipment_id,
        "name": name,
        "category": category,
        "quantity": quantity
    }

    data["equipment"].append(equipment)
    save_data(data)

    print(f"Equipment added successfully. ID: {equipment_id}")


def view_equipment(data):
    if not data["equipment"]:
        print("No equipment found.")
        return

    print("\n--- All Equipment ---")

    for equipment in data["equipment"]:
        borrowed = get_borrowed_quantity(data, equipment["id"])
        available = get_available_quantity(data, equipment)

        print(f"\nID: {equipment['id']}")
        print(f"Name: {equipment['name']}")
        print(f"Category: {equipment['category']}")
        print(f"Total: {equipment['quantity']}")
        print(f"Borrowed: {borrowed}")
        print(f"Available: {available}")


def search_equipment(data):
    keyword = input("Enter equipment name or category: ").strip().casefold()

    if not keyword:
        print("Search term cannot be empty.")
        return

    results = [
        equipment
        for equipment in data["equipment"]
        if keyword in equipment["name"].casefold()
        or keyword in equipment["category"].casefold()
    ]

    if not results:
        print("No matching equipment found.")
        return

    for equipment in results:
        available = get_available_quantity(data, equipment)

        print(
            f"ID: {equipment['id']} | "
            f"Name: {equipment['name']} | "
            f"Category: {equipment['category']} | "
            f"Available: {available}"
        )


def update_equipment(data):
    try:
        equipment_id = int(input("Enter equipment ID to update: "))
    except ValueError:
        print("Invalid ID.")
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

    print("Leave a field empty to keep its current value.")

    name = input(f"New name [{equipment['name']}]: ").strip()
    category = input(
        f"New category [{equipment['category']}]: "
    ).strip()
    quantity_input = input(
        f"New total quantity [{equipment['quantity']}]: "
    ).strip()

    new_quantity = equipment["quantity"]

    if quantity_input:
        try:
            new_quantity = int(quantity_input)

            if new_quantity < 1:
                print("Quantity must be greater than zero.")
                return

        except ValueError:
            print("Please enter a valid quantity.")
            return

    borrowed = get_borrowed_quantity(data, equipment_id)

    if new_quantity < borrowed:
        print(
            f"Cannot set quantity below the borrowed amount ({borrowed})."
        )
        return

    if name:
        equipment["name"] = name

    if category:
        equipment["category"] = category

    equipment["quantity"] = new_quantity

    save_data(data)
    print("Equipment updated successfully.")


def delete_equipment(data):
    try:
        equipment_id = int(input("Enter equipment ID to delete: "))
    except ValueError:
        print("Invalid ID.")
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

    borrowed = get_borrowed_quantity(data, equipment_id)

    if borrowed > 0:
        print("Cannot delete equipment while units are borrowed.")
        return

    data["equipment"].remove(equipment)
    save_data(data)

    print("Equipment deleted successfully.")
