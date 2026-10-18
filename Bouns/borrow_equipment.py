from storage import save_data
from datetime import date


def borrow_equipment(data):
    employee = input("Enter employee name: ")
    equipment_id = input("Enter equipment ID: ")

    try:
        quantity = int(input("Enter quantity to borrow: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    for item in data["equipment"]:

        if str(item["id"]) == equipment_id:

            borrowed = 0

            for transaction in data["transactions"]:
                if (
                    transaction["equipment_id"] == item["id"]
                    and transaction["status"] == "borrowed"
                ):
                    borrowed += transaction["quantity"]

            available = item["quantity"] - borrowed

            if quantity > available:
                print("Not enough equipment available.")
                print("Available quantity:", available)
                return

            if data["transactions"]:
                transaction_id = max(
                    transaction["id"]
                    for transaction in data["transactions"]
                ) + 1
            else:
                transaction_id = 1

            transaction = {
                "id": transaction_id,
                "equipment_id": item["id"],
                "employee": employee,
                "quantity": quantity,
                "date": date.today().isoformat(),
                "status": "borrowed"
            }

            data["transactions"].append(transaction)

            save_data(data)

            print("Equipment borrowed successfully!")
            print("Transaction ID:", transaction_id)
            return

    print("Equipment ID not found.")