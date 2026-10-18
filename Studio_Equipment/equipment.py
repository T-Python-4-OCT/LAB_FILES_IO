"""Equipment CRUD + search."""
from helpers import (read_int, read_text, find_equipment,
                     borrowed_units, print_equipment)
from storage import save_data


def add_equipment(data):
    name = read_text("Name: ")
    category = read_text("Category: ")
    quantity = read_int("Total quantity: ", minimum=1)
    item_id = data["counters"]["equipment"]
    data["counters"]["equipment"] += 1  # never goes back -> IDs are never reused
    data["equipment"].append(
        {"id": item_id, "name": name, "category": category, "quantity": quantity})
    save_data(data)
    print(f"Equipment added with ID {item_id}.")


def view_all(data):
    if not data["equipment"]:
        print("No equipment recorded.")
        return
    for item in data["equipment"]:
        print_equipment(data, item)
        print()


def search_equipment(data):
    term = read_text("Search by name or category: ").lower()
    results = [e for e in data["equipment"]
               if term in e["name"].lower() or term in e["category"].lower()]
    if not results:
        print("No matching equipment.")
    for item in results:
        print_equipment(data, item)
        print()


def update_equipment(data):
    item = find_equipment(data, read_int("Equipment ID: "))
    if item is None:
        print("Equipment not found.")
        return
    print("Press Enter to keep the current value.")
    name = input(f"Name [{item['name']}]: ").strip() or item["name"]
    category = input(f"Category [{item['category']}]: ").strip() or item["category"]
    raw_qty = input(f"Total quantity [{item['quantity']}]: ").strip()
    quantity = item["quantity"]
    if raw_qty:
        try:
            quantity = int(raw_qty)
        except ValueError:
            print("Invalid quantity. Nothing was changed.")
            return
        borrowed = borrowed_units(data, item["id"])
        if quantity < max(1, borrowed):
            print(f"Quantity cannot be below {max(1, borrowed)} "
                  f"({borrowed} unit(s) currently borrowed). Nothing was changed.")
            return
    item.update(name=name, category=category, quantity=quantity)
    save_data(data)
    print("Equipment updated.")


def delete_equipment(data):
    item = find_equipment(data, read_int("Equipment ID: "))
    if item is None:
        print("Equipment not found.")
        return
    borrowed = borrowed_units(data, item["id"])
    if borrowed > 0:
        print(f"Cannot delete: {borrowed} unit(s) are currently borrowed.")
        return
    data["equipment"].remove(item)
    save_data(data)
    print(f"'{item['name']}' deleted.")