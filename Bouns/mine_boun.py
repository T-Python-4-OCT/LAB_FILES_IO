from storage import load_data
from view_equipment import view_equipment
from add_equipment import add_equipment
from search_equipment import search_equipment
from update_equipment import update_equipment
from borrow_equipment import borrow_equipment
from delete_equipment import delete_equipment
from return_equipment import return_equipment
from borrowing_history import view_borrowing_history
data = load_data()

while True:
    print("="*40)
    print("   STUDIO EQUIPMENT MANAGER")
    print("="*40)

    print("1. Add Equipment")
    print("2. View All Equipment")
    print("3. Search Equipment")
    print("4. Update Equipment")
    print("5. Delete Equipment")
    print("6. Borrow Equipment")
    print("7. Return Equipment")
    print("8. View Borrowing History")
    print("9. Exit")

    users = input("Select an option: ")

    if users == "1":
        add_equipment(data)

    elif users == "2":
        view_equipment(data)

    elif users == "3":
        search_equipment(data)

    elif users == "4":
        update_equipment(data)

    elif users == "5":
        delete_equipment(data)

    elif users == "6":
        borrow_equipment(data)

    elif users == "7":
        return_equipment(data)

    elif users == "8":
        view_borrowing_history(data)

    elif users == "9":
        print("See you soon , Goodbye")
        break

    else:
        print("Invalid option. Please try again.")