from storage import save_data
from helpers import read_positive_int, read_text, find_equipment, borrowed_count


def print_equipment(data, item):
    borrowed = borrowed_count(data, item["id"])
    print(f"[ID {item['id']}] {item['name']}  ({item['category']})")
    print(f"    Total: {item['quantity']}")
    print(f"    Borrowed: {borrowed}")
    print(f"    Available: {item['quantity'] - borrowed}")


def add_equipment(data):
    name = read_text("Equipment name: ")
    if name is None:
        return
    category = read_text("Category: ")
    if category is None:
        return
    quantity = read_positive_int("Total quantity: ")
    if quantity is None:
        return

    item = {
        "id": data["next_equipment_id"],
        "name": name,
        "category": category,
        "quantity": quantity,
    }
    data["equipment"].append(item)
    data["next_equipment_id"] += 1
    save_data(data)
    print(f"Added '{name}' with ID {item['id']}.")


def view_all_equipment(data):
    if not data["equipment"]:
        print("There is no equipment yet.")
        return
    for item in data["equipment"]:
        print_equipment(data, item)
        print()


def search_equipment(data):
    term = read_text("Search by name or category: ")
    if term is None:
        return
    term = term.lower()
    matches = [item for item in data["equipment"]
               if term in item["name"].lower() or term in item["category"].lower()]
    if not matches:
        print("No equipment matches your search.")
        return
    for item in matches:
        print_equipment(data, item)
        print()


def update_equipment(data):
    equipment_id = read_positive_int("Equipment ID to update: ")
    if equipment_id is None:
        return
    item = find_equipment(data, equipment_id)
    if item is None:
        print(f"No equipment with ID {equipment_id}.")
        return

    borrowed = borrowed_count(data, equipment_id)
    print("Press Enter to keep the current value.")
    new_name = input(f"Name [{item['name']}]: ").strip() or item["name"]
    new_category = input(f"Category [{item['category']}]: ").strip() or item["category"]

    new_quantity = item["quantity"]
    quantity_text = input(f"Total quantity [{item['quantity']}]: ").strip()
    if quantity_text != "":
        if not (quantity_text.isascii() and quantity_text.isdigit() and int(quantity_text) > 0):
            print("Please enter a whole number greater than 0. Nothing was changed.")
            return
        new_quantity = int(quantity_text)
        if new_quantity < borrowed:
            print(f"{borrowed} unit(s) are currently borrowed, so the total cannot be "
                  f"less than {borrowed}. Nothing was changed.")
            return

    item["name"] = new_name
    item["category"] = new_category
    item["quantity"] = new_quantity
    save_data(data)
    print("Equipment updated.")


def delete_equipment(data):
    equipment_id = read_positive_int("Equipment ID to delete: ")
    if equipment_id is None:
        return
    item = find_equipment(data, equipment_id)
    if item is None:
        print(f"No equipment with ID {equipment_id}.")
        return

    borrowed = borrowed_count(data, equipment_id)
    if borrowed > 0:
        print(f"Cannot delete '{item['name']}': {borrowed} unit(s) are currently borrowed.")
        return

    answer = input(f"Delete '{item['name']}'? (y/n): ").strip().lower()
    if answer != "y":
        print("Deletion cancelled.")
        return

    data["equipment"].remove(item)
    save_data(data)
    print(f"Deleted '{item['name']}'.")