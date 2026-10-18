
from studio_package import (
    load_data,
    add_equipment,
    view_equipment,
    search_equipment,
    update_equipment,
    delete_equipment,
    borrow_equipment,
    return_equipment,
    view_borrowing_history,
)


def display_menu():
    print("""
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
""")


def main():
    data = load_data()

    actions = {
        "1": add_equipment,
        "2": view_equipment,
        "3": search_equipment,
        "4": update_equipment,
        "5": delete_equipment,
        "6": borrow_equipment,
        "7": return_equipment,
        "8": view_borrowing_history,
    }

    while True:
        display_menu()
        choice = input("Select an option: ").strip()

        if choice == "9":
            print("Thank you for using Studio Equipment Manager.")
            break

        action = actions.get(choice)

        if action is None:
            print("Invalid option. Please select from 1 to 9.")
            continue

        try:
            action(data)
        except (OSError, ValueError) as error:
            print(f"Operation failed: {error}")


if __name__ == "__main__":
    main()
