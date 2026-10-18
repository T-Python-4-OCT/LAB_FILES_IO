from Data import load_data
from Operations import (add_equipment, view_all, search_equipment,
                        update_equipment, delete_equipment,
                        borrow_equipment, return_equipment, view_history)

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


def main():
    data = load_data()
    actions = {
        "1": add_equipment,
        "2": view_all,
        "3": search_equipment,
        "4": update_equipment,
        "5": delete_equipment,
        "6": borrow_equipment,
        "7": return_equipment,
        "8": view_history,
    }

    while True:
        print(MENU)
        choice = input("Select an option: ").strip()
        if choice == "9":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(data)
        else:
            print("Invalid option. Please choose 1-9.")


if __name__ == "__main__":
    main()