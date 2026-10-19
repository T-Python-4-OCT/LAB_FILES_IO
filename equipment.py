
from storage import save_data


def get_equipment(data, equipment_id):
    for item in data["equipment"]:
        if item["id"] == equipment_id:
            return item
    return None


def get_borrowed_quantity(data, equipment_id):
    borrowed = 0

    for transaction in data["transactions"]:
        if transaction["equipment_id"] == equipment_id:
            if transaction["status"] == "borrowed":
                borrowed += transaction["quantity"]

    return borrowed


def add_equipment(data):
    name = input("Enter equipment name: ").strip()
    category = input("Enter category: ").strip()

    if not name or not category:
        print("Name and category cannot be empty")
        return

    try:
        quantity = int(input("Enter total quantity: "))
    except ValueError:
        print("Invalid quantity")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero")
        return

    equipment_id = max(
        [item["id"] for item in data["equipment"]],
        default=0
    ) + 1

    data["equipment"].append({
        "id": equipment_id,
        "name": name,
        "category": category,
        "quantity": quantity
    })

    save_data(data)
    print("Equipment added successfully. ID:", equipment_id)


def display_equipment(data):
    if not data["equipment"]:
        print("No equipment found")
        return

    for item in data["equipment"]:
        borrowed = get_borrowed_quantity(data, item["id"])
        available = item["quantity"] - borrowed

        print("*" * 20)
        print("ID:", item["id"])
        print("Name:", item["name"])
        print("Category:", item["category"])
        print("Total:", item["quantity"])
        print("Borrowed:", borrowed)
        print("Available:", available)


def search_equipment(data):
    keyword = input("Enter name or category: ").strip().lower()

    found = False

    for item in data["equipment"]:
        if keyword in item["name"].lower() or keyword in item["category"].lower():
            borrowed = get_borrowed_quantity(data, item["id"])

            print("*" * 20)
            print("ID:", item["id"])
            print("Name:", item["name"])
            print("Category:", item["category"])
            print("Total:", item["quantity"])
            print("Borrowed:", borrowed)
            print("Available:", item["quantity"] - borrowed)
            found = True

    if not found:
        print("Equipment not found")


def update_equipment(data):
    try:
        equipment_id = int(input("Enter equipment ID: "))
    except ValueError:
        print("Invalid ID")
        return

    item = get_equipment(data, equipment_id)

    if item is None:
        print("Equipment not found")
        return

    name = input("Enter new name (blank to keep): ").strip()
    category = input("Enter new category (blank to keep): ").strip()
    quantity_input = input("Enter new quantity (blank to keep): ").strip()

    if quantity_input:
        try:
            quantity = int(quantity_input)
        except ValueError:
            print("Invalid quantity")
            return

        borrowed = get_borrowed_quantity(data, equipment_id)

        if quantity < borrowed or quantity <= 0:
            print("Quantity must be positive and not less than borrowed units")
            return

        item["quantity"] = quantity

    if name:
        item["name"] = name

    if category:
        item["category"] = category

    save_data(data)
    print("Equipment updated successfully")


def delete_equipment(data):
    try:
        equipment_id = int(input("Enter equipment ID: "))
    except ValueError:
        print("Invalid ID")
        return

    item = get_equipment(data, equipment_id)

    if item is None:
        print("Equipment not found")
        return

    if get_borrowed_quantity(data, equipment_id) > 0:
        print("Cannot delete equipment while borrowed")
        return

    data["equipment"].remove(item)
    save_data(data)
    print("Equipment deleted successfully")
