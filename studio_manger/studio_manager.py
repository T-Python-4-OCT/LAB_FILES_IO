

import json
import os
from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "studio_data.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        initial_data = {"equipment": [], "transactions": []}
        save_data(initial_data)
        return initial_data
    
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {"equipment": [], "transactions": []}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def get_available_quantity(equipment_id, data):
    eq = next((e for e in data["equipment"] if e["id"] == equipment_id), None)
    if not eq:
        return 0
    
    total = eq["quantity"]
    borrowed = sum(
        t["quantity"] for t in data["transactions"]
        if t["equipment_id"] == equipment_id and t["status"] == "borrowed"
    )
    return total - borrowed

def add_equipment(data):
    name = input("Enter equipment name: ").strip()
    category = input("Enter category: ").strip()
    try:
        quantity = int(input("Enter total quantity: "))
    except ValueError:
        print("[!] Invalid quantity. Must be a number.\n")
        return

    new_id = 1 if not data["equipment"] else max(e["id"] for e in data["equipment"]) + 1

    eq = {
        "id": new_id,
        "name": name,
        "category": category,
        "quantity": quantity
    }
    data["equipment"].append(eq)
    save_data(data)
    print(f"✓ Equipment added successfully with ID: {new_id}\n")

def view_equipment(data):
    if not data["equipment"]:
        print("[!] No equipment found in the system.\n")
        return

    print("\n=================================")
    print("      ALL EQUIPMENT LIST         ")
    print("=================================")
    for eq in data["equipment"]:
        eq_id = eq["id"]
        total = eq["quantity"]
        borrowed = total - get_available_quantity(eq_id, data)
        available = get_available_quantity(eq_id, data)

        print(f"ID: {eq_id} | Name: {eq['name']} | Category: {eq['category']}")
        print(f"  Total: {total} | Borrowed: {borrowed} | Available: {available}")
        print("-" * 33)
    print()

def search_equipment(data):
    query = input("Enter name or category to search: ").strip().lower()
    results = [
        e for e in data["equipment"]
        if query in e["name"].lower() or query in e["category"].lower()
    ]

    if not results:
        print("[!] No matching equipment found.\n")
        return

    print("\n--- Search Results ---")
    for eq in results:
        eq_id = eq["id"]
        available = get_available_quantity(eq_id, data)
        print(f"ID: {eq_id} | Name: {eq['name']} | Category: {eq['category']} | Available: {available}")
    print()

def update_equipment(data):
    try:
        eq_id = int(input("Enter equipment ID to update: "))
    except ValueError:
        print("[!] Invalid ID.\n")
        return

    eq = next((e for e in data["equipment"] if e["id"] == eq_id), None)
    if not eq:
        print("[!] Equipment not found.\n")
        return

    print(f"Current -> Name: {eq['name']} | Category: {eq['category']} | Quantity: {eq['quantity']}")
    new_name = input("Enter new name (or press Enter to keep current): ").strip()
    new_cat = input("Enter new category (or press Enter to keep current): ").strip()
    new_qty_str = input("Enter new total quantity (or press Enter to keep current): ").strip()

    if new_name:
        eq["name"] = new_name
    if new_cat:
        eq["category"] = new_cat
    if new_qty_str:
        try:
            new_qty = int(new_qty_str)
            borrowed_units = eq["quantity"] - get_available_quantity(eq_id, data)
            if new_qty < borrowed_units:
                print(f"[!] Error: New quantity cannot be less than currently borrowed units ({borrowed_units}).\n")
                return
            eq["quantity"] = new_qty
        except ValueError:
            print("[!] Invalid quantity format. Quantity not changed.\n")

    save_data(data)
    print("✓ Equipment updated successfully!\n")

def delete_equipment(data):
    try:
        eq_id = int(input("Enter equipment ID to delete: "))
    except ValueError:
        print("[!] Invalid ID.\n")
        return

    eq = next((e for e in data["equipment"] if e["id"] == eq_id), None)
    if not eq:
        print("[!] Equipment not found.\n")
        return

    available = get_available_quantity(eq_id, data)
    total = eq["quantity"]
    if available < total:
        print("[!] Cannot delete equipment. Some units are currently borrowed.\n")
        return

    data["equipment"] = [e for e in data["equipment"] if e["id"] != eq_id]
    save_data(data)
    print("✓ Equipment deleted successfully!\n")

def borrow_equipment(data):
    employee = input("Enter employee name: ").strip()
    try:
        eq_id = int(input("Enter equipment ID to borrow: "))
        qty = int(input("Enter quantity to borrow: "))
    except ValueError:
        print("[!] Invalid input.\n")
        return

    eq = next((e for e in data["equipment"] if e["id"] == eq_id), None)
    if not eq:
        print("[!] Equipment not found.\n")
        return

    available = get_available_quantity(eq_id, data)
    if qty > available:
        print(f"[!] Rejected: Only {available} units available. Cannot borrow {qty}.\n")
        return

    trans_id = 1 if not data["transactions"] else max(t["id"] for t in data["transactions"]) + 1

    transaction = {
        "id": trans_id,
        "equipment_id": eq_id,
        "employee": employee,
        "quantity": qty,
        "date": str(date.today()),
        "status": "borrowed"
    }

    data["transactions"].append(transaction)
    save_data(data)
    print(f"✓ Successfully borrowed! Transaction ID is: {trans_id}\n")

def return_equipment(data):
    try:
        trans_id = int(input("Enter borrowing transaction ID to return: "))
    except ValueError:
        print("[!] Invalid transaction ID.\n")
        return

    trans = next((t for t in data["transactions"] if t["id"] == trans_id), None)
    if not trans:
        print("[!] Transaction not found.\n")
        return

    if trans["status"] == "returned":
        print("[!] This transaction has already been returned.\n")
        return

    trans["status"] = "returned"
    save_data(data)
    print("✓ Equipment returned successfully! Units are now available again.\n")

def view_borrowing_history(data):
    if not data["transactions"]:
        print("[!] No borrowing history found.\n")
        return

    print("\n=================================")
    print("      BORROWING HISTORY          ")
    print("=================================")
    for t in data["transactions"]:
        print(f"Transaction ID: {t['id']} | Eq ID: {t['equipment_id']} | Employee: {t['employee']}")
        print(f"  Qty: {t['quantity']} | Date: {t['date']} | Status: {t['status'].upper()}")
        print("-" * 33)
    print()

def main():
    data = load_data()
    while True:
        print("=================================")
        print("    STUDIO EQUIPMENT MANAGER     ")
        print("=================================")
        print("1. Add Equipment")
        print("2. View All Equipment")
        print("3. Search Equipment")
        print("4. Update Equipment")
        print("5. Delete Equipment")
        print("6. Borrow Equipment")
        print("7. Return Equipment")
        print("8. View Borrowing History")
        print("9. Exit")
        
        choice = input("\nSelect an option: ").strip()
        
        if choice == "1":
            add_equipment(data)
        elif choice == "2":
            view_equipment(data)
        elif choice == "3":
            search_equipment(data)
        elif choice == "4":
            update_equipment(data)
        elif choice == "5":
            delete_equipment(data)
        elif choice == "6":
            borrow_equipment(data)
        elif choice == "7":
            return_equipment(data)
        elif choice == "8":
            view_borrowing_history(data)
        elif choice == "9":
            print("Thank you for using Studio Equipment Manager. Goodbye!")
            break
        else:
            print("[!] Invalid option. Please choose between 1 and 9.\n")

if __name__ == "__main__":
    main()