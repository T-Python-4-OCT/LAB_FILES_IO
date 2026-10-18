def search_equipment(data):
    search = input("Enter equipment name or category: ").lower()

    found = False

    for item in data["equipment"]:
        if search in item["name"].lower() or search in item["category"].lower():
            print("="*40)
            print("ID:", item["id"])
            print("Name:", item["name"])
            print("Category:", item["category"])
            print("Total Quantity:", item["quantity"])
            print("="*40)

            found = True
    if not found:
        print("No equipment found.")