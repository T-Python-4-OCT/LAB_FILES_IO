
import json
from pathlib import Path

from functions.equipment_management import (
    add_equipment,
    update_equipment,
    delete_equipment
)

from functions.equipment_view import (
    view_all_equipment,
    search_equipment
)

from functions.equipment_borrow import (
    borrow_equipment,
    return_equipment,
    view_borrowing_history
)


FILE_PATH = Path(__file__).resolve().parent / "studio_data.json"


def save_data(data):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_data():
    if not FILE_PATH.exists():
        data = {
            "equipment": [],
            "transactions": [],
            "next_equipment_id": 1,
            "next_transaction_id": 1
        }
        save_data(data)
        return data

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("Invalid data structure.")

    if not isinstance(data.get("equipment"), list):
        raise ValueError("Invalid equipment records.")

    if not isinstance(data.get("transactions"), list):
        raise ValueError("Invalid transaction records.")

    data.setdefault(
        "next_equipment_id",
        max((item["id"] for item in data["equipment"]), default=0) + 1
    )

    data.setdefault(
        "next_transaction_id",
        max((item["id"] for item in data["transactions"]), default=0) + 1
    )

    return data


def main():
    try:
        data = load_data()
    except (OSError, ValueError) as error:
        print(f"Unable to load studio data: {error}")
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
        changed = False

        if choice == "1":
            changed = add_equipment(data)

        elif choice == "2":
            view_all_equipment(data)

        elif choice == "3":
            search_equipment(data)

        elif choice == "4":
            changed = update_equipment(data)

        elif choice == "5":
            changed = delete_equipment(data)

        elif choice == "6":
            changed = borrow_equipment(data)

        elif choice == "7":
            changed = return_equipment(data)

        elif choice == "8":
            view_borrowing_history(data)

        elif choice == "9":
            print("Thank you for using Studio Equipment Manager!")
            break

        else:
            print("Invalid option! Please try again.")

        if changed:
            try:
                save_data(data)
                print("Changes saved successfully!")
            except OSError as error:
                print(f"Failed to save data: {error}")


if __name__ == "__main__":
    main()
