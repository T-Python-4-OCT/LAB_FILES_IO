
from Funcc import (
    load_data,
    add_equipment,
    view_equipment,
    search_equipment,
    update_equipment,
    delete_equipment,
    borrow_equipment,
    return_equipment,
    view_borrowing_history
)


def main():
    data = load_data()

    while True:
        print("\n===== Studio Equipment Checkout System =====")
        print("1. Add Equipment")
        print("2. View All Equipment")
        print("3. Search Equipment")
        print("4. Update Equipment")
        print("5. Delete Equipment")
        print("6. Borrow Equipment")
        print("7. Return Equipment")
        print("8. View Borrowing History")
        print("9. Exit")

        choice = input("Choose an option: ").strip()

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
            print("Invalid choice! Please select 1-9.")


if __name__ == "__main__":
    main()
