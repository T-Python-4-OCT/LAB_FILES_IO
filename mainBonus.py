from equipment_data import load_data
from equipment_operations import (
    add_equipment,
    borrow_equipment,
    delete_equipment,
    return_equipment,
    search_equipment,
    update_equipment,
    view_all_equipment,
    view_borrowing_history,
)

def main():
    try:
        data = load_data()
    except (OSError, ValueError) as error:
        print(f"Could not load equipment data: {error}")
        return

    actions = {
        "1": add_equipment,
        "2": view_all_equipment,
        "3": search_equipment,
        "4": update_equipment,
        "5": delete_equipment,
        "6": borrow_equipment,
        "7": return_equipment,
        "8": view_borrowing_history,
    }

    while True:
        print(
            "\n=================================\n"
            "    STUDIO EQUIPMENT MANAGER\n"
            "=================================\n"
            "1. Add Equipment\n"
            "2. View All Equipment\n"
            "3. Search Equipment\n"
            "4. Update Equipment\n"
            "5. Delete Equipment\n"
            "6. Borrow Equipment\n"
            "7. Return Equipment\n"
            "8. View Borrowing History\n"
            "9. Exit"
        )
        choice = input("Select an option: ").strip()

        if choice == "9":
            print("Goodbye come back again soon..")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid option. Choose a number from 1 to 9.")
            continue

        try:
            action(data)
        except OSError as error:
            print(f"Could not save equipment data: {error}")
            try:
                latest_data = load_data()
            except (OSError, ValueError) as reload_error:
                print(f"Could not reload equipment data: {reload_error}")
                return
            data.clear()
            data.update(latest_data)


if __name__ == "__main__":
    main()