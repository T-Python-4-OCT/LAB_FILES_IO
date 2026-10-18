from studio.storage import save_data


def generate_equipment_id(data):
    """Generate a new equipment ID."""

    if not data["equipment"]:
        return 1

    last_id = data["equipment"][-1]["id"]

    return last_id + 1


def add_equipment(data, name, quantity):
    """Add new equipment."""

    name = name.strip()

    if name == "":
        print("Equipment name cannot be empty.")
        return

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    equipment_id = generate_equipment_id(data)

    equipment = {
        "id": equipment_id,
        "name": name,
        "quantity": quantity,
        "available": quantity
    }

    data["equipment"].append(equipment)

    save_data(data)

    print(f"Equipment '{name}' added successfully.")
    print(f"Equipment ID: {equipment_id}")


def display_equipment(data):
    """Display all equipment."""

    if not data["equipment"]:
        print("\nNo equipment found.")
        return

    print("\n==============================================")
    print("               STUDIO EQUIPMENT")
    print("==============================================")

    for equipment in data["equipment"]:
        print(f"ID        : {equipment['id']}")
        print(f"Name      : {equipment['name']}")
        print(f"Quantity  : {equipment['quantity']}")
        print(f"Available : {equipment['available']}")
        print("----------------------------------------------")


def search_equipment(data, equipment_id):
    """Search for equipment by ID."""

    for equipment in data["equipment"]:

        if equipment["id"] == equipment_id:
            return equipment

    return None


def delete_equipment(data, equipment_id):
    """Delete equipment."""

    equipment = search_equipment(data, equipment_id)

    if equipment is None:
        print("Equipment not found.")
        return

    data["equipment"].remove(equipment)

    save_data(data)

    print(f"Equipment '{equipment['name']}' deleted successfully.")


def update_equipment(data, equipment_id, new_name, new_quantity):
    """Update equipment."""

    equipment = search_equipment(data, equipment_id)

    if equipment is None:
        print("Equipment not found.")
        return

    new_name = new_name.strip()

    if new_name == "":
        print("Equipment name cannot be empty.")
        return

    if new_quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    borrowed = equipment["quantity"] - equipment["available"]

    if new_quantity < borrowed:
        print("New quantity cannot be less than borrowed quantity.")
        return

    equipment["name"] = new_name
    equipment["quantity"] = new_quantity
    equipment["available"] = new_quantity - borrowed

    save_data(data)

    print("Equipment updated successfully.")


def borrow_equipment(data, equipment_id, borrow_quantity):
    """Borrow a specific quantity of equipment."""

    equipment = search_equipment(data, equipment_id)

    if equipment is None:
        print("Equipment not found.")
        return

    if borrow_quantity <= 0:
        print("Borrow quantity must be greater than 0.")
        return

    if borrow_quantity > equipment["available"]:
        print(
            f"Only {equipment['available']} item(s) are available."
        )
        return

    equipment["available"] -= borrow_quantity

    transaction = {
        "equipment_id": equipment_id,
        "action": "borrow",
        "quantity": borrow_quantity
    }

    data["transactions"].append(transaction)

    save_data(data)

    print(
        f"{borrow_quantity} item(s) of "
        f"'{equipment['name']}' borrowed successfully."
    )


def return_equipment(data, equipment_id, return_quantity):
    """Return a specific quantity of equipment."""

    equipment = search_equipment(data, equipment_id)

    if equipment is None:
        print("Equipment not found.")
        return

    if return_quantity <= 0:
        print("Return quantity must be greater than 0.")
        return

    if equipment["available"] + return_quantity > equipment["quantity"]:
        print("Cannot return more than borrowed quantity.")
        return

    equipment["available"] += return_quantity

    transaction = {
        "equipment_id": equipment_id,
        "action": "return",
        "quantity": return_quantity
    }

    data["transactions"].append(transaction)

    save_data(data)

    print(
        f"{return_quantity} item(s) of "
        f"'{equipment['name']}' returned successfully."
    )


def display_transactions(data):
    """Display transaction history."""

    if not data["transactions"]:
        print("No transactions found.")
        return

    print("\n========================")
    print("     TRANSACTIONS")
    print("========================")

    for transaction in data["transactions"]:
        print(
            f"Equipment ID: {transaction['equipment_id']} "
            f"- Action: {transaction['action']}"
        )