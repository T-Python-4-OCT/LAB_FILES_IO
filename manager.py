from datetime import date
from storage import save_data


def add_equipment(data):
  name = input("Enter equipment name: ")
  category = input("Enter category: ")
  quantity = int(input("Enter total quantity: "))

  new_id = 1
  if data["equipment"]:
    new_id = data["equipment"][-1]["id"] + 1

  eq = {
      "id": new_id,
      "name": name,
      "category": category,
      "quantity": quantity,
  }
  data["equipment"].append(eq)
  save_data(data)
  print(f"Equipment '{name}' added successfully with ID {new_id}.")


def view_equipment(data):
  print("\n--- Studio Equipment ---")
  if not data["equipment"]:
    print("No equipment available.")
    return

  for eq in data["equipment"]:
    eq_id = eq["id"]
    borrowed_qty = sum(
        t["quantity"]
        for t in data["transactions"]
        if t["equipment_id"] == eq_id and t["status"] == "borrowed"
    )
    available_qty = eq["quantity"] - borrowed_qty

    print(f"\n{eq['name']} (ID: {eq_id})")
    print(f"Category: {eq['category']}")
    print(f"Total: {eq['quantity']}")
    print(f"Borrowed: {borrowed_qty}")
    print(f"Available: {available_qty}")
  print("------------------------\n")


def search_equipment(data):
  keyword = input("Enter search keyword (name or category): ").lower()
  found = False
  print("\n--- Search Results ---")
  for eq in data["equipment"]:
    if (
        keyword in eq["name"].lower()
        or keyword in eq["category"].lower()
    ):
      print(f"ID: {eq['id']} | Name: {eq['name']} | Category: {eq['category']} | Total: {eq['quantity']}")
      found = True
  if not found:
    print("No matching equipment found.")
  print("----------------------\n")


def update_equipment(data):
  eq_id = int(input("Enter equipment ID to update: "))
  for eq in data["equipment"]:
    if eq["id"] == eq_id:
      eq["name"] = input(f"Enter new name [{eq['name']}]: ") or eq["name"]
      eq["category"] = input(f"Enter new category [{eq['category']}]: ") or eq["category"]
      new_qty = input(f"Enter new total quantity [{eq['quantity']}]: ")
      if new_qty:
        eq["quantity"] = int(new_qty)
      save_data(data)
      print("Equipment updated successfully.")
      return
  print("Equipment ID not found.")


def delete_equipment(data):
  eq_id = int(input("Enter equipment ID to delete: "))
  for eq in data["equipment"]:
    if eq["id"] == eq_id:
      is_borrowed = any(
          t["equipment_id"] == eq_id and t["status"] == "borrowed"
          for t in data["transactions"]
      )
      if is_borrowed:
        print("Cannot delete equipment because some units are currently borrowed.")
      else:
        data["equipment"] = [e for e in data["equipment"] if e["id"] != eq_id]
        save_data(data)
        print("Equipment deleted successfully.")
      return
  print("Equipment ID not found.")


def borrow_equipment(data):
  name = input("Enter employee name: ")
  eq_id = int(input("Enter equipment ID to borrow: "))
  borrow_qty = int(input("Enter quantity to borrow: "))

  target_eq = None
  for eq in data["equipment"]:
    if eq["id"] == eq_id:
      target_eq = eq
      break

  if not target_eq:
    print("Equipment ID not found.")
    return

  borrowed_qty = sum(
      t["quantity"]
      for t in data["transactions"]
      if t["equipment_id"] == eq_id and t["status"] == "borrowed"
  )
  available_qty = target_eq["quantity"] - borrowed_qty

  if borrow_qty > available_qty:
    print(f"Rejected. Only {available_qty} units are available.")
    return

  new_t_id = 1
  if data["transactions"]:
    new_t_id = data["transactions"][-1]["id"] + 1

  transaction = {
      "id": new_t_id,
      "equipment_id": eq_id,
      "employee": name,
      "quantity": borrow_qty,
      "date": str(date.today()),
      "status": "borrowed",
  }
  data["transactions"].append(transaction)
  save_data(data)
  print(f"Successfully borrowed. Transaction ID: {new_t_id}")


def return_equipment(data):
  t_id = int(input("Enter transaction ID to return: "))
  for t in data["transactions"]:
    if t["id"] == t_id:
      if t["status"] == "returned":
        print("This transaction has already been returned.")
        return
      t["status"] = "returned"
      save_data(data)
      print("Equipment returned successfully.")
      return
  print("Transaction ID not found.")


def view_history(data):
  print("\n--- Borrowing History ---")
  if not data["transactions"]:
    print("No transactions found.")
    return
  for t in data["transactions"]:
    print(f"Transaction ID: {t['id']} | Equipment ID: {t['equipment_id']} | Employee: {t['employee']} | Qty: {t['quantity']} | Date: {t['date']} | Status: {t['status']}")
  print("-------------------------\n")