"""Studio Equipment Manager - run this file:  python main.py"""
from storage import load_data
from equipment import (add_equipment, view_all, search_equipment,
                       update_equipment, delete_equipment)
from borrowing import borrow_equipment, return_equipment, view_history

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

ACTIONS = {
    "1": add_equipment, "2": view_all, "3": search_equipment,
    "4": update_equipment, "5": delete_equipment, "6": borrow_equipment,
    "7": return_equipment, "8": view_history,
}


def main():
    data = load_data()
    while True:
        print(MENU)
        choice = input("Select an option: ").strip()
        if choice == "9":
            print("Goodbye!")
            break
        action = ACTIONS.get(choice)
        if action is None:
            print("Invalid option, please choose 1-9.")
            continue
        action(data)


if __name__ == "__main__":
    main()