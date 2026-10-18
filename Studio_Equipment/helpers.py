"""Input helpers and lookup/calculation functions shared by all modules."""


def read_int(prompt, minimum=None):
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if minimum is not None and value < minimum:
            print(f"  Value must be at least {minimum}.")
            continue
        return value


def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  This field cannot be empty.")


def find_equipment(data, equipment_id):
    return next((e for e in data["equipment"] if e["id"] == equipment_id), None)


def find_transaction(data, transaction_id):
    return next((t for t in data["transactions"] if t["id"] == transaction_id), None)


def borrowed_units(data, equipment_id):
    """Sum of quantities in this equipment's transactions still 'borrowed'."""
    return sum(t["quantity"] for t in data["transactions"]
               if t["equipment_id"] == equipment_id and t["status"] == "borrowed")


def available_units(data, item):
    return item["quantity"] - borrowed_units(data, item["id"])


def print_equipment(data, item):
    borrowed = borrowed_units(data, item["id"])
    print(f"[ID {item['id']}] {item['name']}  ({item['category']})")
    print(f"    Total: {item['quantity']}")
    print(f"    Borrowed: {borrowed}")
    print(f"    Available: {item['quantity'] - borrowed}")