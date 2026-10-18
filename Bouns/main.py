from storage import load_data, save_data

from equipment.manager import (
    add_equipment,
    view_equipment,
    search_equipment,
    update_equipment,
    delete_equipment
)

from equipment.borrowing import (
    borrow_equipment,
    return_equipment,
    view_history
)


data = load_data()


def show_menu():
    print("=" * 33)
    print("    STUDIO EQUIPMENT MANAGER")
    print("=" * 33)
    print("1. Add Equipment")
    print("2. View All Equipment")
    print("3. Search Equipment")
    print("4. Update Equipment")
    print("5. Delete Equipment")
    print("6. Borrow Equipment")
    print("7. Return Equipment")
    print("8. View Borrowing History")
    print("9. Exit")



while True:
    show_menu()
    choice = input("Select an option: ")
    

    if choice == "9":
        print("Thank you for using Studio Equipment Manager!")
        break

    elif choice == "1":
        name = input("Enter equipment name: ")
        category = input("Enter equipment category: ")
        quantity = int(input("Enter total quantity: "))

        item = add_equipment(data, name, category, quantity)
        save_data(data)
        print(f"Equipment added successfully! ID: {item['id']}")

    elif choice == "2":
        
        view_equipment(data)

    
    elif choice == "3":
        keyword = input("Enter equipment name or category: ")
        search_equipment(data, keyword)


    
    elif choice == "4":
        equipment_id = int(input("Enter equipment ID to update: "))
        name = input("Enter new name (press Enter to skip): ")
        category = input("Enter new category (press Enter to skip): ")
        quantity_input = input("Enter new quantity (press Enter to skip): ")

        quantity = int(quantity_input) if quantity_input else None

        updated = update_equipment(
            data, equipment_id,
            name or None,
            category or None,
            quantity
        )

        if updated:
            save_data(data)
            print("Equipment updated successfully!")
        else:
            print("Equipment not found!")


    
    elif choice == "5":
        equipment_id = int(input("Enter equipment ID to delete: "))

        deleted = delete_equipment(data, equipment_id)

        if deleted:
            save_data(data)
            print("Equipment deleted successfully!")
        else:
            print("Cannot delete equipment. Check the ID or active borrowings.")

    elif choice == "6":
        employee = input("Enter employee name: ")
        equipment_id = int(input("Enter equipment ID: "))
        quantity = int(input("Enter quantity to borrow: "))

        transaction = borrow_equipment(
            data, employee, equipment_id, quantity
        )

        if transaction:
            save_data(data)
            print(f"Equipment borrowed successfully! Transaction ID: {transaction['id']}")
        else:
            print("Borrowing failed. Check the equipment ID, quantity, and availability.")

    elif choice == "7":
        transaction_id = int(input("Enter transaction ID to return: "))

        returned = return_equipment(data, transaction_id)

        if returned:
            save_data(data)
            print("Equipment returned successfully!")
        else:
            print("Return failed. Check the transaction ID or its status.")

    elif choice == "8":
        view_history(data)

    else:
        print("Invalid option. Please choose from 1 to 9.")
