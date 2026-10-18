# ==================================================
# ABDULRAHMAN STUDIO MANAGER 🎬
# Borrowing & Return Center 📦
# ==================================================

from datetime import date
from equipment import available_count


def borrow_item(items, records):
    """Borrow equipment from the studio."""

    print("\n--- Borrow Equipment 📤")

    employee = input("Employee name: ")

    try:
        target = int(input("Equipment ID: "))
        amount = int(input("Quantity: "))

    except ValueError:
        print("Invalid input.❌")
        return False

    if amount <= 0:
        print("Quantity must be greater than 0.❌")
        return False

    found = None

    for item in items:

        if item["id"] == target:
            found = item
            break

    if found is None:
        print("Equipment not found. ❌")
        return False

    available = available_count(
        found,
        records
    )

    if amount > available:
        print(
            f"Not enough equipment available. "
            f"Available: {available} ❌"
        )
        return False

    transaction_id = max(
        (record["id"] for record in records),
        default=0
    ) + 1

    record = {
        "id": transaction_id,
        "employee": employee,
        "equipment_id": target,
        "quantity": amount,
        "date": str(date.today()),
        "status": "borrowed"
    }

    records.append(record)

    print("Borrowed successfully! ✅")
    print(f"Transaction ID: {transaction_id}🆔")

    return True


def return_item(records):
    """Return previously borrowed equipment."""

    print("\n--- Return Equipment ---📥")

    try:
        target = int(input("Transaction ID: "))

    except ValueError:
        print("Invalid ID❌")
        return False

    for record in records:

        if record["id"] == target:

            if record["status"] == "returned":
                print(
                    "This transaction was already returned.⚠️"
                )
                return False

            record["status"] = "returned"

            print("Equipment returned successfully.✅")

            return True
    print("Transaction not found.❌")

    return False


def show_history(records):
    """Display all borrowing transactions."""

    print("\n--- Borrowing History -📜")

    if not records:
        print("No borrowing history📭")
        return

    for record in records:

        print(
            f'\nTransaction: {record["id"]} 🆔'
            f'\nEmployee: {record["employee"]}👤'
            f'\nEquipment ID: {record["equipment_id"]}🎥'
            f'\nQuantity: {record["quantity"]}📦'
            f'\nDate: {record["date"]}📅'
            f'\nStatus: {record["status"]} 📌'
        )