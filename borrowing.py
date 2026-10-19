from datetime import date
from equipment import find_equipment, get_available, get_next_id, read_int


def borrow_equipment(data):
    employee = input("Employee name: ").strip()
    equipment_id = read_int("Equipment ID: ")
    quantity = read_int("Quantity: ")

    if not employee:
        print("Employee name cannot be empty.")
        return False
    item = find_equipment(data, equipment_id)
    if item is None:
        print("Equipment not found.")
        return False
    if quantity is None or quantity <= 0:
        print("Quantity must be a positive number.")
        return False

    available = get_available(data, item)
    if quantity > available:
        print(f"Rejected: only {available} available.")
        return False

    transaction = {
        "id": get_next_id(data["transactions"]),
        "equipment_id": equipment_id,
        "employee": employee,
        "quantity": quantity,
        "date": date.today().isoformat(),
        "status": "borrowed",
    }
    data["transactions"].append(transaction)
    print(f"Borrowed. Transaction ID: {transaction['id']}")
    return True


def return_equipment(data):
    transaction_id = read_int("Transaction ID: ")
    for t in data["transactions"]:
        if t["id"] == transaction_id:
            if t["status"] == "returned":
                print("This transaction was already returned.")
                return False
            t["status"] = "returned"
            print("Returned successfully.")
            return True
    print("Transaction not found.")
    return False


def view_history(data):
    if not data["transactions"]:
        print("No transactions yet.")
        return
    for t in data["transactions"]:
        item = find_equipment(data, t["equipment_id"])
        name = item["name"] if item else "Deleted equipment"
        print(f"#{t['id']} | {name} | {t['employee']} | "
              f"qty {t['quantity']} | {t['date']} | {t['status']}")