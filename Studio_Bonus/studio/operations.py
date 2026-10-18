from datetime import date
from .storage import write_data


def read_number(prompt, minimum=1):
    while True:
        text = input(prompt).strip()
        if text.isdigit() and int(text) >= minimum:
            return int(text)
        print("Enter a valid number.")


def read_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Cannot be empty.")


def get_item(data, item_id):
    for item in data["equipment"]:
        if item["id"] == item_id:
            return item


def get_record(data, record_id):
    for record in data["transactions"]:
        if record["id"] == record_id:
            return record


def units_out(data, item_id):
    return sum(r["quantity"] for r in data["transactions"]
               if r["equipment_id"] == item_id and r["status"] == "borrowed")


def units_free(data, item):
    return item["quantity"] - units_out(data, item["id"])


def show_item(data, item):
    out = units_out(data, item["id"])
    print(f"[{item['id']}] {item['name']} ({item['category']})")
    print(f"    Total: {item['quantity']}")
    print(f"    Borrowed: {out}")
    print(f"    Available: {item['quantity'] - out}")


def add_item(data):
    name = read_text("Name: ")
    category = read_text("Category: ")
    quantity = read_number("Total quantity: ")
    item_id = data["next_equipment_id"]
    data["next_equipment_id"] += 1
    data["equipment"].append({"id": item_id, "name": name, "category": category, "quantity": quantity})
    write_data(data)
    print(f"Added, ID {item_id}.")


def list_items(data):
    if not data["equipment"]:
        print("Nothing here yet.")
    for item in data["equipment"]:
        show_item(data, item)


def find_items(data):
    word = read_text("Search: ").lower()
    results = [i for i in data["equipment"] if word in i["name"].lower() or word in i["category"].lower()]
    if not results:
        print("No results.")
    for item in results:
        show_item(data, item)


def update_item(data):
    item = get_item(data, read_number("Equipment ID: "))
    if item is None:
        print("ID not found.")
        return
    print("Press Enter to keep the old value.")
    name = input(f"Name [{item['name']}]: ").strip()
    category = input(f"Category [{item['category']}]: ").strip()
    quantity = input(f"Quantity [{item['quantity']}]: ").strip()
    new_quantity = item["quantity"]
    if quantity:
        if not quantity.isdigit() or int(quantity) < 1:
            print("Invalid quantity.")
            return
        new_quantity = int(quantity)
        if new_quantity < units_out(data, item["id"]):
            print("Less than the borrowed units.")
            return
    item["name"] = name or item["name"]
    item["category"] = category or item["category"]
    item["quantity"] = new_quantity
    write_data(data)
    print("Updated.")


def remove_item(data):
    item = get_item(data, read_number("Equipment ID: "))
    if item is None:
        print("ID not found.")
    elif units_out(data, item["id"]) > 0:
        print("Cannot delete, units are borrowed.")
    else:
        data["equipment"].remove(item)
        write_data(data)
        print("Deleted.")


def borrow_item(data):
    employee = read_text("Employee: ")
    item = get_item(data, read_number("Equipment ID: "))
    if item is None:
        print("ID not found.")
        return
    quantity = read_number("Quantity: ")
    free = units_free(data, item)
    if quantity > free:
        print(f"Rejected: only {free} available.")
        return
    record_id = data["next_transaction_id"]
    data["next_transaction_id"] += 1
    data["transactions"].append({"id": record_id, "equipment_id": item["id"], "employee": employee,
                                 "quantity": quantity, "date": date.today().isoformat(), "status": "borrowed"})
    write_data(data)
    print(f"Done. Transaction ID: {record_id}. Available: {free - quantity}.")


def return_item(data):
    record = get_record(data, read_number("Transaction ID: "))
    if record is None:
        print("ID not found.")
    elif record["status"] == "returned":
        print("Already returned.")
    else:
        record["status"] = "returned"
        write_data(data)
        print("Returned.")


def show_history(data):
    if not data["transactions"]:
        print("No history yet.")
    for r in data["transactions"]:
        item = get_item(data, r["equipment_id"])
        name = item["name"] if item else f"(deleted #{r['equipment_id']})"
        print(f"#{r['id']}  {r['date']}  {r['employee']}  {name} x{r['quantity']}  [{r['status']}]")