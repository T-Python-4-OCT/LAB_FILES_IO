from storage import load_data, save_data
from equipment import (add_equipment, view_all, search_equipment,
                       update_equipment, delete_equipment)
from borrowing import borrow_equipment, return_equipment, view_history


def show_menu():
    print("=================================")
    print("    STUDIO EQUIPMENT MANAGER")
    print("=================================")
    print()
    print("1. Add Equipment")
    print("2. View All Equipment")
    print("3. Search Equipment")
    print("4. Update Equipment")
    print("5. Delete Equipment")
    print("6. Borrow Equipment")
    print("7. Return Equipment")
    print("8. View Borrowing History")
    print("9. Exit")


def main():
    data = load_data()

    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            changed = add_equipment(data)
        elif choice == "2":
            view_all(data)
            changed = False
        elif choice == "3":
            search_equipment(data)
            changed = False
        elif choice == "4":
            changed = update_equipment(data)
        elif choice == "5":
            changed = delete_equipment(data)
        elif choice == "6":
            changed = borrow_equipment(data)
        elif choice == "7":
            changed = return_equipment(data)
        elif choice == "8":
            view_history(data)
            changed = False
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
            changed = False

        if changed:
            save_data(data)
        print()


main()