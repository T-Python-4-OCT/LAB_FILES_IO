def get_next_id(items):
    if not items:
        return 1
    return max(item["id"] for item in items) + 1


def find_equipment(data, equipment_id):
    for item in data["equipment"]:
        if item["id"] == equipment_id:
            return item
    return None


def get_borrowed_count(data, equipment_id):
    total = 0
    for t in data["transactions"]:
        if t["equipment_id"] == equipment_id and t["status"] == "borrowed":
            total += t["quantity"]
    return total


def get_available(data, equipment):
    return equipment["quantity"] - get_borrowed_count(data, equipment["id"])


def read_int(message):
    try:
        return int(input(message))
    except ValueError:
        return None


def add_equipment(data):
    name = input("Name: ").strip()
    category = input("Category: ").strip()
    quantity = read_int("Total quantity: ")

    if not name or not category:
        print("Name and category cannot be empty.")
        return False
    if quantity is None or quantity <= 0:
        print("Quantity must be a positive number.")
        return False

    item = {
        "id": get_next_id(data["equipment"]),
        "name": name,
        "category": category,
        "quantity": quantity,
    }
    data["equipment"].append(item)
    print(f"Added with ID {item['id']}.")
    return True


def print_item(data, item):
    borrowed = get_borrowed_count(data, item["id"])
    print(f"[{item['id']}] {item['name']} ({item['category']})")
    print(f"    Total: {item['quantity']}")
    print(f"    Borrowed: {borrowed}")
    print(f"    Available: {item['quantity'] - borrowed}")


def view_all(data):
    if not data["equipment"]:
        print("No equipment yet.")
        return
    for item in data["equipment"]:
        print_item(data, item)


def search_equipment(data):
    text = input("Search: ").strip().lower()
    found = False
    for item in data["equipment"]:
        if text in item["name"].lower() or text in item["category"].lower():
            print_item(data, item)
            found = True
    if not found:
        print("No results.")


def update_equipment(data):
    equipment_id = read_int("Equipment ID: ")
    item = find_equipment(data, equipment_id)
    if item is None:
        print("Equipment not found.")
        return False

    print("Leave empty to keep the current value.")
    name = input(f"Name [{item['name']}]: ").strip()
    category = input(f"Category [{item['category']}]: ").strip()
    qty_text = input(f"Total quantity [{item['quantity']}]: ").strip()

    new_quantity = item["quantity"]
    if qty_text:
        try:
            new_quantity = int(qty_text)
        except ValueError:
            print("Quantity must be a number.")
            return False
        borrowed = get_borrowed_count(data, item["id"])
        if new_quantity <= 0 or new_quantity < borrowed:
            print(f"Quantity must be positive and at least {borrowed} (currently borrowed).")
            return False

    if name:
        item["name"] = name
    if category:
        item["category"] = category
    item["quantity"] = new_quantity
    print("Updated.")
    return True


def delete_equipment(data):
    equipment_id = read_int("Equipment ID: ")
    item = find_equipment(data, equipment_id)
    if item is None:
        print("Equipment not found.")
        return False
    if get_borrowed_count(data, item["id"]) > 0:
        print("Cannot delete: some units are currently borrowed.")
        return False
    data["equipment"].remove(item)
    print("Deleted.")
    return True