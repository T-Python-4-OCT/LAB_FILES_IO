from studio.storeg import save_data


def get_equipment(data, equipment_id):
    for item in data["equipment"]:
        if item["id"] == equipment_id:
            return item
    return None


def get_borrowed_quantity(data, equipment_id):
    total = 0

    for transaction in data["transactions"]:
        if (
            transaction["equipment_id"] == equipment_id
            and transaction["status"] == "borrowed"
        ):
            total += transaction["quantity"]

    return total


def get_available_quantity(data, item):
    return item["quantity"] - get_borrowed_quantity(
        data, item["id"]
    )


def get_positive_integer(message):
    while True:
        try:
            number = int(input(message))

            if number > 0:
                return number

            print("Enter a number greater than zero.")

        except ValueError:
            print("Enter a valid whole number.")


def add_equipment(data):
    name = input("Equipment name: ").strip()
    category = input("Category: ").strip()

    if not name or not category:
        print("Name and category cannot be empty.")
        return

    quantity = get_positive_integer("Total quantity: ")

    item = {
        "id": data["next_equipment_id"],
        "name": name,
        "category": category,
        "quantity": quantity
    }

    data["equipment"].append(item)
    data["next_equipment_id"] += 1

    save_data(data)
    print("Equipment added. ID:", item["id"])



def view_equipment(data):
    equipment_list = data.get("equipment", [])

    if not equipment_list:
        print("No equipment found.")
        return

    for item in equipment_list:
        borrowed = get_borrowed_quantity(data, item["id"])
        available = item["quantity"] - borrowed

        print("\n==============================")
        print("ID:", item["id"])
        print("Name:", item["name"])
        print("Category:", item["category"])
        print("Total:", item["quantity"])
        print("Borrowed:", borrowed)
        print("Available:", available)
        print("==============================")



def search_equipment(data):
    keyword = input("Search name or category: ").strip().lower()

    if not keyword:
        print("Enter a search term.")
        return

    found = False

    for item in data["equipment"]:
        if (
            keyword in item["name"].lower()
            or keyword in item["category"].lower()
        ):
            print("\nID:", item["id"])
            print("Name:", item["name"])
            print("Category:", item["category"])
            print("Total:", item["quantity"])
            print("Borrowed:", get_borrowed_quantity(data, item["id"]))
            print("Available:", get_available_quantity(data, item))
            found = True

    if not found:
        print("No matching equipment found.")


def update_equipment(data):
    equipment_id = get_positive_integer("Equipment ID: ")
    item = get_equipment(data, equipment_id)

    if item is None:
        print("Equipment not found.")
        return

    print("Leave a field empty to keep its current value.")

    name = input("New name: ").strip()
    category = input("New category: ").strip()
    quantity_input = input("New total quantity: ").strip()

    new_quantity = item["quantity"]

    if quantity_input:
        try:
            new_quantity = int(quantity_input)
        except ValueError:
            print("Invalid quantity. Nothing changed.")
            return

        borrowed = get_borrowed_quantity(data, equipment_id)

        if new_quantity < 1 or new_quantity < borrowed:
            print("Quantity cannot be less than borrowed units.")
            return

    if name:
        item["name"] = name

    if category:
        item["category"] = category

    item["quantity"] = new_quantity

    save_data(data)
    print("Equipment updated successfully.")


def delete_equipment(data):
    equipment_id = get_positive_integer("Equipment ID: ")
    item = get_equipment(data, equipment_id)

    if item is None:
        print("Equipment not found.")
        return

    if get_borrowed_quantity(data, equipment_id) > 0:
        print("Cannot delete equipment while units are borrowed.")
        return

    data["equipment"].remove(item)

    save_data(data)
    print("Equipment deleted successfully.")
