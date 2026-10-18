from datetime import date
from databasee import save_data
from equipment import get_available_quantity


def borrow_equipment(data):
  print("\n--- Borrow Equipment ---")
  employee = input("Enter employee name: ").strip()
  try:
    eq_id = int(input("Enter equipment ID to borrow: "))
    qty = int(input("Enter quantity to borrow: "))
  except ValueError:
    print("Invalid input format.")
    return

  if qty <= 0:
    print("Quantity must be greater than zero.")
    return

  target_item = next(
      (item for item in data["equipment"] if item["id"] == eq_id), None
  )
  if not target_item:
    print("Equipment ID not found.")
    return

  available = get_available_quantity(eq_id, data)
  if qty > available:
    print(
        f"Rejected: Only {available} units available, but you requested"
        f" {qty}."
    )
    return

  tx_id = max((tx["id"] for tx in data["transactions"]), default=0) + 1
  new_tx = {
      "id": tx_id,
      "equipment_id": eq_id,
      "employee": employee,
      "quantity": qty,
      "date": str(date.today()),
      "status": "borrowed",
  }

  data["transactions"].append(new_tx)
  save_data(data)
  print(f"Success! Transaction ID {tx_id}: Borrowed {qty} unit(s).")


def return_equipment(data):
  print("\n--- Return Equipment ---")
  try:
    tx_id = int(input("Enter transaction ID to return: "))
  except ValueError:
    print("Invalid transaction ID.")
    return

  target_tx = next(
      (tx for tx in data["transactions"] if tx["id"] == tx_id), None
  )
  if not target_tx:
    print("Transaction ID not found.")
    return

  if target_tx["status"] == "returned":
    print("This transaction has already been returned.")
    return

  target_tx["status"] = "returned"
  save_data(data)
  print(f"Transaction ID {tx_id} successfully marked as returned!")


def view_history(data):
  print("\n--- Borrowing History ---")
  if not data["transactions"]:
    print("No borrowing history recorded.")
    return

  for tx in data["transactions"]:
    print(
        f"Tx ID: {tx['id']} | Eq ID: {tx['equipment_id']} | Employee:"
        f" {tx['employee']} | Qty: {tx['quantity']} | Date: {tx['date']} |"
        f" Status: {tx['status']}"
    )
    print("-" * 50)