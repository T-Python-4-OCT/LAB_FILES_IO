
from studio.storeg import load_data
from studio.equipment import (
    add_equipment,
    view_equipment,
    search_equipment,
    update_equipment,
    delete_equipment
)
from studio.transactions import (
    borrow_equipment,
    return_equipment,
    view_borrowing_history
)


def main():
    try:
        data = load_data()
    except (OSError, ValueError, TypeError, KeyError) as error:
        print("Could not load studio_data.json.")
        print("Check the file before running again:", error)
        return

    while True:
        print("\n=================================")
        print("    STUDIO EQUIPMENT MANAGER")
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

        try:
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
                print("Goodbye!")
                break

            else:
                print("Invalid option. Choose 1-9.")

        except (OSError, TypeError, KeyError) as error:
            print("Operation failed:", error)


if __name__ == "__main__":
    main()
