from storage import save_data
def add_equipment(data):
    name = input("Enter equipment name: ")
    category = input("Enter equipment category: ")
    quantity = int(input("Enter total quantity: "))

    if data["equipment"]:
        new_id = max(item["id"] for item in data["equipment"]) + 1
    else:
        new_id = 1

    equipment = {
        "id": new_id,
        "name": name,
        "category": category,
        "quantity": quantity
    }

    data["equipment"].append(equipment)

    save_data(data)

    print("Equipment added successfully!")
    print("Equipment ID:", new_id)