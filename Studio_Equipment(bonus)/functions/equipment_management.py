
def add_equipment(data):
    name = input("Equipment name: ").strip()
    category = input("Category: ").strip()

    if not name or not category:
        print("Name and category cannot be empty.")
        return False

    try:
        quantity = int(input("Total quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return False

    except ValueError:
        print("Please enter a valid number.")
        return False

    equipment_id = data["next_equipment_id"]

    equipment = {
        "id": equipment_id,
        "name": name,
        "category": category,
        "quantity": quantity
    }

    data["equipment"].append(equipment)
    data["next_equipment_id"] += 1

    print(f"Equipment added successfully! ID: {equipment_id}")
    return True


def update_equipment(data):
    try:
        equipment_id = int(input("Enter equipment ID: "))
    except ValueError:
        print("Invalid equipment ID.")
        return False

    for equipment in data["equipment"]:
        if equipment["id"] == equipment_id:

            print(f"Current name: {equipment['name']}")
            print(f"Current category: {equipment['category']}")
            print(f"Current quantity: {equipment['quantity']}")
            print("Press Enter to keep the current value.")

            name = input("New name: ").strip()
            category = input("New category: ").strip()
            quantity_input = input("New total quantity: ").strip()

            new_name = name if name else equipment["name"]
            new_category = category if category else equipment["category"]
            new_quantity = equipment["quantity"]

            if quantity_input:
                try:
                    new_quantity = int(quantity_input)
                except ValueError:
                    print("Invalid quantity.")
                    return False

            borrowed = 0

            for transaction in data["transactions"]:
                if (transaction["equipment_id"] == equipment_id
                        and transaction["status"] == "borrowed"):
                    borrowed += transaction["quantity"]

            if new_quantity < borrowed or new_quantity < 0:
                print(f"Invalid quantity. {borrowed} units are borrowed.")
                return False

            if (new_name == equipment["name"]
                    and new_category == equipment["category"]
                    and new_quantity == equipment["quantity"]):
                print("No changes made.")
                return False

            equipment["name"] = new_name
            equipment["category"] = new_category
            equipment["quantity"] = new_quantity

            print("Equipment updated successfully!")
            return True

    print("Equipment not found.")
    return False


def delete_equipment(data):
    try:
        equipment_id = int(input("Enter equipment ID: "))
    except ValueError:
        print("Invalid equipment ID.")
        return False

    for equipment in data["equipment"]:
        if equipment["id"] == equipment_id:

            borrowed = 0

            for transaction in data["transactions"]:
                if (transaction["equipment_id"] == equipment_id
                        and transaction["status"] == "borrowed"):
                    borrowed += transaction["quantity"]

            if borrowed > 0:
                print("Cannot delete equipment while units are borrowed.")
                return False

            print(f"Equipment: {equipment['name']}")
            confirm = input("Delete this equipment? (y/n): ").strip().lower()

            if confirm != "y":
                print("Deletion cancelled.")
                return False

            data["equipment"].remove(equipment)

            print("Equipment deleted successfully!")
            return True

    print("Equipment not found.")
    return False
