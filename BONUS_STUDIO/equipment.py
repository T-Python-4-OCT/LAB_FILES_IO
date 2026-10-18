# ==================================================
# ABDULRAHMAN STUDIO MANAGER 🎬
# Equipment Control Center 🎥
# ==================================================


def available_count(item, records):
    """Calculate the number of available units."""

    borrowed = 0

    for record in records:
        if (
            record["equipment_id"] == item["id"]
            and record["status"] == "borrowed"
        ):
            borrowed += record["quantity"]

    return item["total"] - borrowed


def add_equipment(items):
    """Add a new equipment item."""

    print("\n--- Add New Equipment - 🎥")

    name = input("Equipment name: ")
    category = input("Category: ")

    try:
        total = int(input("Total quantity: "))

        if total <= 0:
            print("Quantity must be greater than 0. ❌")
            return False

    except ValueError:
        print("Invalid quantity.❌")
        return False

    new_id = max(
        (item["id"] for item in items),
        default=0
    ) + 1

    items.append({
        "id": new_id,
        "name": name,
        "category": category,
        "total": total
    })

    print(f"Equipment added successfully! ID: {new_id}  ✅")

    return True


def show_equipment(items, records):
    """Display all studio equipment."""

    print("\n--- Studio Equipment 🎬")

    if not items:
        print("No equipment found. 📭")
        return

    for item in items:
        available = available_count(item, records)
        borrowed = item["total"] - available

        print(
            f'\nID: {item["id"]} 🎥'
            f'\nName: {item["name"]}'
            f'\nCategory: {item["category"]}'
            f'\nTotal: {item["total"]}'
            f'\nBorrowed: {borrowed}   📤'
            f'\nAvailable: {available}  📥'
        )


def find_equipment(items):
    """Search equipment by name or category."""

    print("\n--- Search Equipment ---🔎")

    word = input("Search: ").lower()
    found = False

    for item in items:
        if (
            word in item["name"].lower()
            or word in item["category"].lower()
        ):
            print(
                f'\nID: {item["id"]} 🎥'
                f'\nName: {item["name"]}'
                f'\nCategory: {item["category"]}'
                f'\nTotal: {item["total"]}'
            )

            found = True

    if not found:
        print("Equipment not found.❌")


def edit_equipment(items, records):
    """Update equipment information."""

    print("\n--- Update Equipment --- ✏️")

    try:
        target = int(input("Equipment ID: "))

    except ValueError:
        print("Invalid ID. ❌")
        return False

    for item in items:

        if item["id"] == target:

            name = input("New name: ")
            category = input("New category: ")

            try:
                total = int(input("New total: "))

            except ValueError:
                print("Invalid quantity.❌")
                return False

            borrowed = item["total"] - available_count(
                item,
                records
            )

            if total < borrowed:
                print(
                    "Total cannot be less than "
                    "the borrowed quantity.❌"
                )
                return False

            item["name"] = name
            item["category"] = category
            item["total"] = total

            print("Equipment updated successfully.✅")

            return True

    print("Equipment not found.❌")

    return False


def remove_equipment(items, records):
    """Delete equipment when no units are borrowed."""

    print("\n--- Delete Equipment ---🗑️")

    try:
        target = int(input("Equipment ID: "))

    except ValueError:
        print("Invalid ID.❌")
        return False

    for item in items:

        if item["id"] == target:

            if available_count(item, records) < item["total"]:
                print(
                    "Cannot delete equipment while "
                    "it is borrowed.❌"
                )
                return False

            items.remove(item)

            print("Equipment deleted successfully✅")

            return True

    print("Equipment not found.❌")

    return False