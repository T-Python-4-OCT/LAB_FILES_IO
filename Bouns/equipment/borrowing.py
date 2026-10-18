from datetime import date


def get_next_id(items):
    if not items:
        return 1

    return max(item["id"] for item in items) + 1


def borrow_equipment(data, employee, equipment_id, quantity):
    equipment = None

    for item in data["equipment"]:
        if item["id"] == equipment_id:
            equipment = item
            break

    if equipment is None or quantity <= 0:
        return False

    borrowed = sum(
        transaction["quantity"]
        for transaction in data["transactions"]
        if transaction["equipment_id"] == equipment_id
        and transaction["status"] == "borrowed"
    )

    available = equipment["quantity"] - borrowed

    if quantity > available:
        return False

    transaction = {
        "id": get_next_id(data["transactions"]),
        "equipment_id": equipment_id,
        "employee": employee,
        "quantity": quantity,
        "date": str(date.today()),
        "status": "borrowed"
    }

    data["transactions"].append(transaction)
    return transaction

def return_equipment(data, transaction_id):
    for transaction in data["transactions"]:
        if transaction["id"] == transaction_id:

            if transaction["status"] == "returned":
                return False

            transaction["status"] = "returned"
            return True

    return False

def view_history(data):
    if not data["transactions"]:
        print("No borrowing history found.")
        return

    for transaction in data["transactions"]:
        print(f"Transaction ID: {transaction['id']}")
        print(f"Employee: {transaction['employee']}")
        print(f"Equipment ID: {transaction['equipment_id']}")
        print(f"Quantity: {transaction['quantity']}")
        print(f"Date: {transaction['date']}")
        print(f"Status: {transaction['status']}")
        print("-" * 20)