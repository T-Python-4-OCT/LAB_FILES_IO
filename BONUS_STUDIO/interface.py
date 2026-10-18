# ==================================================
# ABDULRAHMAN STUDIO MANAGER 🎬
# User Interface & Navigation🖥️
# ==================================================

from data import save_data

from equipment import (
    add_equipment,
    show_equipment,
    find_equipment,
    edit_equipment,
    remove_equipment
)

from borrowing import (
    borrow_item,
    return_item,
    show_history
)


def show_menu():
    """Display the main studio menu."""

    print("\n")
    print("╔═══════════════════════")
    print("║ABDULRAHMAN STUDIO MANAGER")
    print("╠═══════════════════════    ")
    print("║ 1. Add Equipment🎥")
    print("║ 2. View All Equipment📋")
    print("║ 3. Search Equipment🔎")
    print("║ 4. Update Equipment✏️ ")
    print("║ 5. Delete Equipment🗑️ ")
    print("║ 6. Borrow Equipment📤 ")
    print("║ 7. Return Equipment📥 ")
    print("║ 8. View Borrowing History📜 ")
    print("║ 9. Exit 🚪 ")
    print("╚══════════════════════════")


def start(data):
    """Start the Studio Equipment Manager."""

    while True:

        show_menu()

        choice = input("\nChoose an option: ")

        if choice == "1":

            if add_equipment(data["equipment"]):
                save_data(data)

        elif choice == "2":

            show_equipment(
                data["equipment"],
                data["transactions"]
            )

        elif choice == "3":

            find_equipment(
                data["equipment"]
            )

        elif choice == "4":

            if edit_equipment(
                data["equipment"],
                data["transactions"]
            ):
                save_data(data)

        elif choice == "5":

            if remove_equipment(
                data["equipment"],
                data["transactions"]
            ):
                save_data(data)

        elif choice == "6":

            if borrow_item(
                data["equipment"],
                data["transactions"]
            ):
                save_data(data)

        elif choice == "7":

            if return_item(
                data["transactions"]
            ):
                save_data(data)

        elif choice == "8":

            show_history(
                data["transactions"]
            )

        elif choice == "9":

            print("\nThank you for using")
            print("ABDULRAHMAN STUDIO MANAGER🎬")
            print("See you next time!👋")

            break

        else:

            print("Invalid choice❌")