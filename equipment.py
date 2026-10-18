from databasee import save_data


def get_available_quantity(equipment_id, data):
  eq_item = None
  for item in data["equipment"]:
    if item["id"] == equipment_id:
      eq_item = item
      break

  if not eq_item:
    return 0

  total = eq_item["quantity"]
  borrowed = 0

  for tx in data["transactions"]:
    if tx["equipment_id"] == equipment_id and tx["status"] == "borrowed":
      borrowed += tx["quantity"]

  return total - borrowed


def add_equipment(data):
  print("\n--- Add New Equipment ---")
  name = input("Enter equipment name: ").strip()
  category = input("Enter equipment category: ").strip()

  try:
    quantity = int(input("Enter total quantity: "))
    if quantity < 0:
      print("Quantity cannot be negative.")
      return
  except ValueError:
    print("Invalid quantity.")
    return

  new_id = max((item["id"] for item in data["equipment"]), default=0) + 1

  new_item = {
      "id": new_id,
      "name": name,
      "category": category,
      "quantity": quantity,
  }
  data["equipment"].append(new_item)
  save_data(data)
  print(f"Equipment '{name}' added successfully with ID {new_id}!")


def view_equipment(data):
  print("\n--- All Studio Equipment ---")
  if not data["equipment"]:
    print("No equipment available.")
    return

  for item in data["equipment"]:
    eq_id = item["id"]
    total = item["quantity"]
    borrowed = total - get_available_quantity(eq_id, data)
    available = get_available_quantity(eq_id, data)

    print(f"ID: {eq_id} | Name: {item['name']} | Category: {item['category']}")
    print(f"  Total: {total} | Borrowed: {borrowed} | Available: {available}")
    print("-" * 40)


def search_equipment(data):
  print("\n--- Search Equipment ---")
  keyword = input("Enter name or category to search: ").strip().lower()

  found = False
  for item in data["equipment"]:
    if (
        keyword in item["name"].lower()
        or keyword in item["category"].lower()
    ):
      eq_id = item["id"]
      total = item["quantity"]
      available = get_available_quantity(eq_id, data)
      print(
          f"ID: {eq_id} | Name: {item['name']} | Category:"
          f" {item['category']} | Available: {available}/{total}"
      )
      found = True

  if not found:
    print("No matching equipment found.")


def update_equipment(data):
  print("\n--- Update Equipment ---")
  try:
    eq_id = int(input("Enter equipment ID to update: "))
  except ValueError:
    print("Invalid ID.")
    return

  target_item = next(
      (item for item in data["equipment"] if item["id"] == eq_id), None
  )
  if not target_item:
    print("Equipment ID not found.")
    return

  new_name = input(
      "Enter new name (leave blank to keep current): "
  ).strip()
  new_cat = input(
      "Enter new category (leave blank to keep current): "
  ).strip()
  qty_input = input(
      "Enter new total quantity (leave blank to keep current): "
  ).strip()

  if new_name:
    target_item["name"] = new_name
  if new_cat:
    target_item["category"] = new_cat
  if qty_input:
    try:
      new_qty = int(qty_input)
      borrowed = target_item["quantity"] - get_available_quantity(eq_id, data)
      if new_qty < borrowed:
        print("Error: New total cannot be less than currently borrowed units.")
        return
      target_item["quantity"] = new_qty
    except ValueError:
      print("Invalid quantity format.")
      return

  save_data(data)
  print("Equipment updated successfully!")


def delete_equipment(data):
  print("\n--- Delete Equipment ---")
  try:
    eq_id = int(input("Enter equipment ID to delete: "))
  except ValueError:
    print("Invalid ID.")
    return

  target_item = next(
      (item for item in data["equipment"] if item["id"] == eq_id), None
  )
  if not target_item:
    print("Equipment ID not found.")
    return

  borrowed = target_item["quantity"] - get_available_quantity(eq_id, data)
  if borrowed > 0:
    print("Cannot delete: Units are currently borrowed.")
    return

  data["equipment"].remove(target_item)
  save_data(data)
  print("Equipment deleted successfully!")