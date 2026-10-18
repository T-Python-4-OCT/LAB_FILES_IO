
from storage import save_data


def get_borrowed_quantity(data, equipment_id):
    """Calculate the quantity currently borrowed."""
    borrowed = 0

    for transaction in data["transactions"]:
        if (transaction["equipment_id"] == equipment_id
                and transaction["status"] == "borrowed"):
            borrowed = borrowed + transaction["quantity"]

    return borrowed


def add_equipment(data):
    """Add new equipment."""
    name = input("Enter equipment name: ")
    category = input("Enter equipment category: ")

    while True:
        try:
            quantity = int(input("Enter total quantity: "))

            if quantity > 0:
                break

            print("Quantity must be greater than zero.")

        except ValueError:
            print("Please enter a whole number.")

    equipment_id = 1

    for item in data["equipment"]:
        if item["id"] >= equipment_id:
            equipment_id = item["id"] + 1

    for transaction in data["transactions"]:
        if transaction["equipment_id"] >= equipment_id:
            equipment_id = transaction["equipment_id"] + 1

    equipment = {
        "id": equipment_id,
        "name": name,
        "category": category,
        "quantity": quantity
    }

    data["equipment"].append(equipment)
    save_data(data)

    print("Equipment added successfully.")
    print("Equipment ID:", equipment_id)


def view_equipment(data):
    """Display all equipment and availability."""
    if len(data["equipment"]) == 0:
        print("No equipment found.")
        return

    for item in data["equipment"]:
        borrowed = get_borrowed_quantity(data, item["id"])
        available = item["quantity"] - borrowed

        print("\nEquipment ID:", item["id"])
        print("Name:", item["name"])
        print("Category:", item["category"])
        print("Total:", item["quantity"])
        print("Borrowed:", borrowed)
        print("Available:", available)


def search_equipment(data):
    """Search equipment by name or category."""
    search = input("Enter equipment name or category: ").lower()
    found = False

    for item in data["equipment"]:
        if (search in item["name"].lower()
                or search in item["category"].lower()):
            borrowed = get_borrowed_quantity(data, item["id"])
            available = item["quantity"] - borrowed

            print("\nEquipment ID:", item["id"])
            print("Name:", item["name"])
            print("Category:", item["category"])
            print("Available:", available)

            found = True

    if not found:
        print("No matching equipment found.")


def update_equipment(data):
    """Update equipment details."""
    try:
        equipment_id = int(input("Enter equipment ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for item in data["equipment"]:
        if item["id"] == equipment_id:
            print("Press Enter to keep the current value.")

            name = input("Enter new name: ")
            category = input("Enter new category: ")
            quantity_text = input("Enter new total quantity: ")

            quantity = item["quantity"]

            if quantity_text != "":
                try:
                    quantity = int(quantity_text)
                except ValueError:
                    print("Please enter a whole number.")
                    return

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    return

                borrowed = get_borrowed_quantity(data, equipment_id)

                if quantity < borrowed:
                    print("Quantity cannot be less than borrowed units.")
                    return

            if name != "":
                item["name"] = name

            if category != "":
                item["category"] = category

            item["quantity"] = quantity

            save_data(data)
            print("Equipment updated successfully.")
            return

    print("Equipment not found.")


def delete_equipment(data):
    """Delete equipment that has no active loans."""
    try:
        equipment_id = int(input("Enter equipment ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for item in data["equipment"]:
        if item["id"] == equipment_id:
            borrowed = get_borrowed_quantity(data, equipment_id)

            if borrowed > 0:
                print("Cannot delete equipment while units are borrowed.")
                return

            data["equipment"].remove(item)
            save_data(data)

            print("Equipment deleted successfully.")
            return

    print("Equipment not found.")
