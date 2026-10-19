
from storage import load_data
from equipment import (
    add_equipment,
    display_equipment,
    search_equipment,
    update_equipment,
    delete_equipment
)
from borrowing import (
    borrow_equipment,
    return_equipment,
    view_borrowing_history
)


def main():
    data = load_data()

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


        choice = input("\nSelect an option: ")

        if choice == "1":
            add_equipment(data)

        elif choice == "2":
            display_equipment(data)

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
            print("Thank you for using Studio Equipment Manager!")
            break

        else:
            print("Invalid option. Please try again.")


main()
