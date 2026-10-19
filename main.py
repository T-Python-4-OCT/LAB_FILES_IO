from manager import (
    add_equipment,
    borrow_equipment,
    delete_equipment,
    return_equipment,
    search_equipment,
    update_equipment,
    view_equipment,
    view_history,
)
from storage import load_data


def main():
  data = load_data()
  while True:
    print("================================")
    print("     STUDIO EQUIPMENT MANAGER")
    print("================================")
    print("1. Add Equipment")
    print("2. View All Equipment")
    print("3. Search Equipment")
    print("4. Update Equipment")
    print("5. Delete Equipment")
    print("6. Borrow Equipment")
    print("7. Return Equipment")
    print("8. View Borrowing History")
    print("9. Exit")

    choice = input("Select an option: ")

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
      view_history(data)
    elif choice == "9":
      print("Exiting program. Goodbye!")
      break
    else:
      print("Invalid choice, please try again.")


if __name__ == "__main__":
  main()