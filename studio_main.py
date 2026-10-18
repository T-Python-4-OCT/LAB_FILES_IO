from studio.storage import load_data

from studio.equipment import (
    add_equipment,
    display_equipment,
    search_equipment,
    delete_equipment,
    update_equipment,
    borrow_equipment,
    return_equipment,
    display_transactions
)


data = load_data()


while True:
    print("\n========================")
    print("      STUDIO MENU")
    print("========================")
    print("1. Add equipment")
    print("2. Display equipment")
    print("3. Search equipment")
    print("4. Update equipment")
    print("5. Delete equipment")
    print("6. Borrow equipment")
    print("7. Return equipment")
    print("8. Display transactions")
    print("9. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number only.")
        continue


    if choice == 1:
        name = input("Enter equipment name: ")

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Quantity must be a number.")
            continue

        add_equipment(data, name, quantity)


    elif choice == 2:
        display_equipment(data)


    elif choice == 3:
        try:
            equipment_id = int(input("Enter equipment ID: "))
        except ValueError:
            print("ID must be a number.")
            continue

        equipment = search_equipment(data, equipment_id)

        if equipment is None:
            print("Equipment not found.")

        else:
            print(f"\nID        : {equipment['id']}")
            print(f"Name      : {equipment['name']}")
            print(f"Quantity  : {equipment['quantity']}")
            print(f"Available : {equipment['available']}")


    elif choice == 4:
        try:
            equipment_id = int(input("Enter equipment ID: "))
        except ValueError:
            print("ID must be a number.")
            continue

        new_name = input("Enter new name: ")

        try:
            new_quantity = int(input("Enter new quantity: "))
        except ValueError:
            print("Quantity must be a number.")
            continue

        update_equipment(
            data,
            equipment_id,
            new_name,
            new_quantity
        )


    elif choice == 5:
        try:
            equipment_id = int(input("Enter equipment ID: "))
        except ValueError:
            print("ID must be a number.")
            continue

        delete_equipment(data, equipment_id)


    elif choice == 6:
        try:
            equipment_id = int(input("Enter equipment ID: "))
            borrow_quantity = int(input("Enter quantity to borrow: "))
        except ValueError:
            print("Please enter numbers only.")
            continue

        borrow_equipment(
            data,
            equipment_id,
            borrow_quantity
        )


    elif choice == 7:
        try:
            equipment_id = int(input("Enter equipment ID: "))
            return_quantity = int(input("Enter quantity to return: "))
        except ValueError:
            print("Please enter numbers only.")
            continue

        return_equipment(
            data,
            equipment_id,
            return_quantity
        )


    elif choice == 8:
        display_transactions(data)


    elif choice == 9:
        print("Program ended.")
        break


    else:
        print("Invalid choice.")