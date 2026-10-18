def view_equipment(data):
    if not data["equipment"]:
        print("No equipment found.")
        return

    for item in data["equipment"]:
        borrowed = 0

        for transaction in data["transactions"]:
            if transaction["equipment_id"] == item["id"] and transaction["status"] == "borrowed":
                borrowed += transaction["quantity"]

        available = item["quantity"] - borrowed

        print("="*40)
        print("ID:", item["id"])
        print("Name:", item["name"])
        print("Category:", item["category"])
        print("Total Quantity:", item["quantity"])
        print("Borrowed:", borrowed)
        print("Available:", available)
        print("="*40)