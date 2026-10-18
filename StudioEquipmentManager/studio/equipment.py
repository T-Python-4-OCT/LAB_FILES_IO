
from .storage import save_data


def find_equipment(data, equipment_id):
    for item in data["equipment"]:
        if item["id"] == equipment_id:
            return item

    return None


def borrowed_quantity(data, equipment_id):
    total = 0

    for transaction in data["transactions"]:
        if (
            transaction["equipment_id"] == equipment_id
            and transaction["status"] == "borrowed"
        ):
            total += transaction["quantity"]

    return total


def available_quantity(data, item):
    return item["quantity"] - borrowed_quantity(data, item["id"])


def get_integer(message, minimum=1):
    while True:
        try:
            number = int(input(message))

            if number < minimum:
                print(f"Enter a number greater than or equal to {minimum}.")
            else:
                return number

        except ValueError:
            print("Please enter a valid whole number.")


def add_equipment(data):
    name = input("Equipment name: ").strip()
    category = input("Category: ").strip()

    if not name or not category:
        print("Name and category cannot be empty.")
        return

    quantity = get_integer("Total quantity: ")

    equipment = {
        "id": data["next_equipment_id"],
        "name": name,
        "category": category,
        "quantity": quantity
    }

    data["equipment"].append(equipment)
    data["next_equipment_id"] += 1

    save_data(data)

    print(f"Equipment added successfully. ID: {equipment['id']}")


def view_equipment(data):
    if not data["equipment"]:
        print("No equipment found.")
        return

    for item in data["equipment"]:
        borrowed = borrowed_quantity(data, item["id"])
        available = available_quantity(data, item)

        print("\n-------------------------")
        print(f"ID: {item['id']}")
        print(f"Name: {item['name']}")
        print(f"Category: {item['category']}")
        print(f"Total: {item['quantity']}")
        print(f"Borrowed: {borrowed}")
        print(f"Available: {available}")


def search_equipment(data):
    keyword = input("Search by name or category: ").strip().lower()

    found = False

    for item in data["equipment"]:
        if (
            keyword in item["name"].lower()
            or keyword in item["category"].lower()
        ):
            print(
                f"ID: {item['id']} | "
                f"Name: {item['name']} | "
                f"Category: {item['category']} | "
                f"Available: {available_quantity(data, item)}"
            )

            found = True

    if not found:
        print("No matching equipment found.")


def update_equipment(data):
    equipment_id = get_integer("Equipment ID: ")
    item = find_equipment(data, equipment_id)

    if item is None:
        print("Equipment not found.")
        return

    print("1. Update name")
    print("2. Update category")
    print("3. Update total quantity")

    choice = input("Select an option: ")

    if choice == "1":
        value = input("New name: ").strip()

        if not value:
            print("Name cannot be empty.")
            return

        item["name"] = value

    elif choice == "2":
        value = input("New category: ").strip()

        if not value:
            print("Category cannot be empty.")
            return

        item["category"] = value

    elif choice == "3":
        quantity = get_integer("New total quantity: ", minimum=0)
        borrowed = borrowed_quantity(data, equipment_id)

        if quantity < borrowed:
            print("Quantity cannot be less than the borrowed amount.")
            return

        item["quantity"] = quantity

    else:
        print("Invalid option.")
        return

    save_data(data)
    print("Equipment updated successfully.")


def delete_equipment(data):
    equipment_id = get_integer("Equipment ID: ")
    item = find_equipment(data, equipment_id)

    if item is None:
        print("Equipment not found.")
        return

    if borrowed_quantity(data, equipment_id) > 0:
        print("Cannot delete equipment while units are borrowed.")
        return

    data["equipment"].remove(item)
    save_data(data)

    print("Equipment deleted successfully.")