import storage
import equipment
import borrowing


def show_menu():
    print()
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
    print()


def main():
    data = storage.load_data()
    actions = {
        "1": equipment.add_equipment,
        "2": equipment.view_all_equipment,
        "3": equipment.search_equipment,
        "4": equipment.update_equipment,
        "5": equipment.delete_equipment,
        "6": borrowing.borrow_equipment,
        "7": borrowing.return_equipment,
        "8": borrowing.view_history,
    }

    while True:
        show_menu()
        choice = input("Select an option: ").strip()
        if choice == "9":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid option. Choose a number from 1 to 9.")
        else:
            action(data)


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")