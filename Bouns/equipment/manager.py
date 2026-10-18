def add_equipment(data, name, category, quantity):
    equipment = {
        "id": get_next_id(data["equipment"]),
        "name": name,
        "category": category,
        "quantity": quantity
    }

    data["equipment"].append(equipment)
    return equipment


def get_next_id(items):
    if not items:
        return 1

    return max(item["id"] for item in items) + 1

def view_equipment(data):
    for item in data["equipment"]:
        borrowed = sum(
            transaction["quantity"]
            for transaction in data["transactions"]
            if transaction["equipment_id"] == item["id"]
            and transaction["status"] == "borrowed"
        )

        available = item["quantity"] - borrowed

        print(f"ID: {item['id']}")
        print(f"Name: {item['name']}")
        print(f"Category: {item['category']}")
        print(f"Total: {item['quantity']}")
        print(f"Borrowed: {borrowed}")
        print(f"Available: {available}")
        print("-" * 20)


def search_equipment(data, keyword):
    for item in data["equipment"]:
        if (keyword.lower() in item["name"].lower()
                or keyword.lower() in item["category"].lower()):
            print(item)


def update_equipment(data, equipment_id, name=None, category=None, quantity=None):
    for item in data["equipment"]:
        if item["id"] == equipment_id:
            if name:
                item["name"] = name
            if category:
                item["category"] = category
            if quantity is not None:
                item["quantity"] = quantity

            return True

    return False


def delete_equipment(data, equipment_id):
    for item in data["equipment"]:
        if item["id"] == equipment_id:
            borrowed = sum(
                transaction["quantity"]
                for transaction in data["transactions"]
                if transaction["equipment_id"] == equipment_id
                and transaction["status"] == "borrowed"
            )

            if borrowed > 0:
                return False

            data["equipment"].remove(item)
            return True

    return False