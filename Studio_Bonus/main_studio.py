from studio.storage import read_data
from studio import operations as ops


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

ACTIONS = {"1": ops.add_item, "2": ops.list_items, "3": ops.find_items, "4": ops.update_item,
           "5": ops.remove_item, "6": ops.borrow_item, "7": ops.return_item, "8": ops.show_history}


def run():
    data = read_data()
    while True:
        print(MENU)
        choice = input("Select an option: ").strip()
        if choice == "9":
            print("Goodbye.")
            break
        action = ACTIONS.get(choice)
        if action:
            action(data)
        else:
            print("Please choose a number from 1 to 9.")


if __name__ == "__main__":
    run()