
def view_all_equipment(data):
    if not data["equipment"]:
        print("No equipment available.")
        return

    print("\n===== ALL EQUIPMENT =====")

    for equipment in data["equipment"]:
        borrowed = 0

        for transaction in data["transactions"]:
            if (transaction["equipment_id"] == equipment["id"]
                    and transaction["status"] == "borrowed"):
                borrowed += transaction["quantity"]

        available = equipment["quantity"] - borrowed

        print(f"\nID: {equipment['id']}")
        print(f"Name: {equipment['name']}")
        print(f"Category: {equipment['category']}")
        print(f"Total: {equipment['quantity']}")
        print(f"Borrowed: {borrowed}")
        print(f"Available: {available}")
        print("-" * 30)


def search_equipment(data):
    search = input("Enter equipment name or category: ").strip().lower()

    if not search:
        print("Search cannot be empty.")
        return

    found = False

    for equipment in data["equipment"]:
        if (search in equipment["name"].lower()
                or search in equipment["category"].lower()):

            found = True
            borrowed = 0

            for transaction in data["transactions"]:
                if (transaction["equipment_id"] == equipment["id"]
                        and transaction["status"] == "borrowed"):
                    borrowed += transaction["quantity"]

            available = equipment["quantity"] - borrowed

            print(f"\nID: {equipment['id']}")
            print(f"Name: {equipment['name']}")
            print(f"Category: {equipment['category']}")
            print(f"Total: {equipment['quantity']}")
            print(f"Borrowed: {borrowed}")
            print(f"Available: {available}")
            print("-" * 30)

    if not found:
        print("No matching equipment found.")
