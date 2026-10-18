from datetime import date
from Data import (save_data, find_equipment, find_transaction,
                  borrowed_count, available_count)

 
def read_text(prompt):
  
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def read_int(prompt, minimum=1):
   
    while True:
        raw = input(prompt).strip()
        try:
            number = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if number < minimum:
            print(f"The number must be at least {minimum}.")
            continue
        return number


def print_equipment(data, item):
    borrowed = borrowed_count(data, item["id"])
    print(f"[ID {item['id']}] {item['name']}  (Category: {item['category']})")
    print(f"    Total: {item['quantity']}")
    print(f"    Borrowed: {borrowed}")
    print(f"    Available: {item['quantity'] - borrowed}")


# 
def add_equipment(data):
    print("\n--- Add Equipment ---")
    name = read_text("Name: ")
    category = read_text("Category: ")
    quantity = read_int("Total quantity: ", 1)

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


def view_all(data):
    print("\n--- All Equipment ---")
    if not data["equipment"]:
        print("No equipment recorded yet.")
        return
    for item in data["equipment"]:
        print_equipment(data, item)
        print()


def search_equipment(data):
    print("\n--- Search Equipment ---")
    term = read_text("Search by name or category: ").lower()
    results = [
        item for item in data["equipment"]
        if term in item["name"].lower() or term in item["category"].lower()
    ]
    if not results:
        print("No matching equipment found.")
        return
    for item in results:
        print_equipment(data, item)
        print()


def update_equipment(data):
    print("\n--- Update Equipment ---")
    item = find_equipment(data, read_int("Equipment ID: ", 1))
    if item is None:
        print("Equipment not found.")
        return

    print_equipment(data, item)
    print("\nPress Enter to keep the current value.")

    new_name = input(f"New name [{item['name']}]: ").strip() or item["name"]
    new_category = input(f"New category [{item['category']}]: ").strip() or item["category"]

    new_quantity = item["quantity"]
    raw_qty = input(f"New total quantity [{item['quantity']}]: ").strip()
    if raw_qty:
        try:
            new_quantity = int(raw_qty)
        except ValueError:
            print("Invalid quantity. Nothing was changed.")
            return
        borrowed = borrowed_count(data, item["id"])
        if new_quantity < max(1, borrowed):
            print(f"Quantity cannot be lower than {max(1, borrowed)} "
                  f"({borrowed} unit(s) are currently borrowed). Nothing was changed.")
            return

    item["name"] = new_name
    item["category"] = new_category
    item["quantity"] = new_quantity
    save_data(data)
    print("Equipment updated.")


def delete_equipment(data):
    print("\n--- Delete Equipment ---")
    item = find_equipment(data, read_int("Equipment ID: ", 1))
    if item is None:
        print("Equipment not found.")
        return

    borrowed = borrowed_count(data, item["id"])
    if borrowed > 0:
        print(f"Cannot delete: {borrowed} unit(s) are currently borrowed.")
        return

    data["equipment"].remove(item)
    save_data(data)
    print(f"Deleted '{item['name']}'.")


 
def borrow_equipment(data):
    print("\n--- Borrow Equipment ---")
    employee = read_text("Employee name: ")
    item = find_equipment(data, read_int("Equipment ID: ", 1))
    if item is None:
        print("Equipment not found.")
        return

    available = available_count(data, item)
    print(f"'{item['name']}': {available} unit(s) available.")
    quantity = read_int("Quantity to borrow: ", 1)

    if quantity > available:
        print(f"Rejected: only {available} unit(s) available.")
        return

    tx = {
        "id": data["next_transaction_id"],
        "equipment_id": item["id"],
        "equipment_name": item["name"],  # keeps history readable even if item is deleted
        "employee": employee,
        "quantity": quantity,
        "date": date.today().isoformat(),
        "status": "borrowed",
    }
    data["transactions"].append(tx)
    data["next_transaction_id"] += 1
    save_data(data)
    print(f"Success! Transaction ID: {tx['id']}  (keep it to return the equipment)")


def return_equipment(data):
    print("\n--- Return Equipment ---")
    tx = find_transaction(data, read_int("Transaction ID: ", 1))
    if tx is None:
        print("Transaction not found.")
        return
    if tx["status"] == "returned":
        print("This transaction was already returned. Nothing changed.")
        return

    tx["status"] = "returned"
    save_data(data)
    print(f"Returned {tx['quantity']} unit(s) from {tx['employee']}.")


def view_history(data):
    print("\n--- Borrowing History ---")
    if not data["transactions"]:
        print("No transactions yet.")
        return
    for tx in data["transactions"]:
        item = find_equipment(data, tx["equipment_id"])
        name = item["name"] if item else tx.get("equipment_name", "(deleted equipment)")
        print(f"[T{tx['id']}] {tx['date']} | {tx['employee']} | "
              f"{name} (ID {tx['equipment_id']}) x{tx['quantity']} | {tx['status']}")