from equipment import (
    add_equipment,
    view_equipment,
    search_equipment,
    update_equipment,
    delete_equipment
)

from transactions import (
    borrow_equipment,
    return_equipment,
    view_transactions
)


def main():
    while True:
        print("\n===================================")
        print(" Studio Equipment Manager")
        print("===================================")
        print("1. Add Equipment")
        print("2. View Equipment")
        print("3. Search Equipment")
        print("4. Update Equipment")
        print("5. Delete Equipment")
        print("6. Borrow Equipment")
        print("7. Return Equipment")
        print("8. View Transaction History")
        print("9. Exit")
        print("===================================")

        choice = input("Select an option (1-9): ").strip()

        if choice == "1":
            add_equipment()

        elif choice == "2":
            view_equipment()

        elif choice == "3":
            search_equipment()

        elif choice == "4":
            update_equipment()

        elif choice == "5":
            delete_equipment()

        elif choice == "6":
            borrow_equipment()

        elif choice == "7":
            return_equipment()

        elif choice == "8":
            view_transactions()

        elif choice == "9":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()
