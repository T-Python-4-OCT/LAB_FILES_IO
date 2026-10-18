import logic
from storage import load, save

MENU = """
=================================
    STUDIO EQUIPMENT MANAGER
=================================

1. Add Equipment
2. View All Equipment
3. Search Equipment
4. Update Equipment
5. Delete Equipment
6. Borrow Equipment
7. Return Equipment
8. View Borrowing History
9. Exit
"""


def num(prompt):
    """Whole number, or 0 if the input is invalid (the logic rejects 0 with a clear message)."""
    s = input(prompt).strip()
    return int(s) if s.isdigit() else 0


def done(data, result):
    ok, msg = result
    print(msg)
    if ok:
        save(data)  # every successful change is saved immediately


def show(data, items):
    for e in items:
        used = logic.out(data, e["id"])
        print(f"\n[{e['id']}] {e['name']} ({e['category']})\n    Total: {e['quantity']}"
              f"\n    Borrowed: {used}\n    Available: {e['quantity'] - used}")
    if not items:
        print("No equipment found.")


def update(d):
    eid = num("Equipment ID: ")
    name = input("New name (Enter to keep): ").strip()
    cat = input("New category (Enter to keep): ").strip()
    s = input("New total quantity (Enter to keep): ").strip()
    done(d, logic.update(d, eid, name, cat, int(s) if s.isdigit() else (0 if s else None)))


def history(d):
    for t in d["transactions"]:
        eq = logic.find(d["equipment"], t["equipment_id"])
        print(f"#{t['id']} | {t['employee']} | {eq['name'] if eq else 'deleted item'} x{t['quantity']}"
              f" | {t['date']} | {t['status']}")
    if not d["transactions"]:
        print("No borrowing history yet.")


ACTIONS = {
    "1": lambda d: done(d, logic.add(d, input("Name: ").strip(), input("Category: ").strip(), num("Total quantity: "))),
    "2": lambda d: show(d, d["equipment"]),
    "3": lambda d: show(d, logic.search(d, input("Search name or category: "))),
    "4": update,
    "5": lambda d: done(d, logic.delete(d, num("Equipment ID to delete: "))),
    "6": lambda d: done(d, logic.borrow(d, input("Employee name: ").strip(), num("Equipment ID: "), num("Quantity: "))),
    "7": lambda d: done(d, logic.give_back(d, num("Transaction ID: "))),
    "8": history,
}

data = load()
while True:
    print(MENU)
    try:
        choice = input("Select an option: ").strip()
    except EOFError:
        break
    if choice == "9":
        print("Goodbye!")
        break
    ACTIONS.get(choice, lambda d: print("Invalid option, choose 1 to 9."))(data)



#MohammedAlnsafi