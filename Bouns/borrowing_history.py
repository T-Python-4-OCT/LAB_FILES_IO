def view_borrowing_history(data):
    if not data["transactions"]:
        print("No borrowing history found.")
        return

    for transaction in data["transactions"]:
        print("="*40)
        print("Transaction ID:", transaction["id"])
        print("Equipment ID:", transaction["equipment_id"])
        print("Employee:", transaction["employee"])
        print("Quantity:", transaction["quantity"])
        print("Date:", transaction["date"])
        print("Status:", transaction["status"])
        print("="*40)