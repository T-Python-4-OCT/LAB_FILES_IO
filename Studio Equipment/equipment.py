from data_file import save_data
from tools import read_number, find_equipment, get_borrowed, show_equipment


def add_equipment(data):
    name = input("Equipment name: ")
    category = input("Category: ")
    quantity = read_number("Total quantity: ")

    if name == "" or category == "" or quantity == 0:
        print("Name and category cannot be empty, and quantity must be more than 0")
        return

    #the ID counter is saved in the file and only goes up,
    #so two records never get the same ID (even after deleting)
    new_item = {
        "id": data["next_equipment_id"],
        "name": name,
        "category": category,
        "quantity": quantity
    }
    data["equipment"].append(new_item)
    data["next_equipment_id"] = data["next_equipment_id"] + 1
    save_data(data)
    print("Equipment added with ID", new_item["id"])


def view_all_equipment(data):
    if len(data["equipment"]) == 0:
        print("No equipment yet")
        return
    for item in data["equipment"]:
        show_equipment(data, item)


def search_equipment(data):
    word = input("Search by name or category: ").lower()
    found = False
    for item in data["equipment"]:
        if word in item["name"].lower() or word in item["category"].lower():
            show_equipment(data, item)
            found = True
    if not found:
        print("No equipment found")


def update_equipment(data):
    equipment_id = read_number("Equipment ID to update: ")
    item = find_equipment(data, equipment_id)
    if item is None:
        print("No equipment with this ID")
        return

    show_equipment(data, item)
    print("Press Enter to keep the old value")
    new_name = input("New name: ")
    new_category = input("New category: ")
    new_quantity = input("New total quantity: ")

    if new_quantity != "":
        if not new_quantity.isdigit():
            print("Quantity must be a number, nothing was changed")
            return
        borrowed = get_borrowed(data, item["id"])
        if int(new_quantity) == 0 or int(new_quantity) < borrowed:
            print("Quantity cannot be 0 or less than the borrowed units (" + str(borrowed) + "), nothing was changed")
            return
        item["quantity"] = int(new_quantity)

    if new_name != "":
        item["name"] = new_name
    if new_category != "":
        item["category"] = new_category

    save_data(data)
    print("Equipment updated")


def delete_equipment(data):
    equipment_id = read_number("Equipment ID to delete: ")
    item = find_equipment(data, equipment_id)
    if item is None:
        print("No equipment with this ID")
        return

    if get_borrowed(data, equipment_id) > 0:
        print("Cannot delete, some units are still borrowed")
        return

    data["equipment"].remove(item)
    save_data(data)
    print(item["name"], "deleted")
