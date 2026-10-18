from storage import save_data


def update_equipment(data):
    equipment_id = input("Enter equipment ID to update: ")

    for item in data["equipment"]:
        if str(item["id"]) == equipment_id:

            print("Current Name:", item["name"])
            print("Current Category:", item["category"])
            print("Current Quantity:", item["quantity"])

            name = input("Enter new name: ")
            category = input("Enter new category: ")
            quantity = int(input("Enter new total quantity: "))

            borrowed = 0

            for transaction in data["transactions"]:
                if transaction["equipment_id"] == item["id"] and transaction["status"] == "borrowed":
                    borrowed += transaction["quantity"]

            if quantity < borrowed:
                print("Error: Quantity cannot be less than borrowed quantity.")
                return

            item["name"] = name
            item["category"] = category
            item["quantity"] = quantity

            save_data(data)

            print("Equipment updated successfully!")
            return
    print("Equipment ID not found.")