from todo_package import add_todo, list_todos


while True:
    choice = input(   "\nDo you want to add a new To-Do item? (y/n/exit): ").lower().strip()

    if choice == "exit":
        print("thank you for using the To-Do program, "  "come back again soon" )
        break

    elif choice == "y":
        add_todo()

    elif choice == "n":
        view_list = input("Do you want to list your To-Do items? (y/n): ").lower().strip()

        if view_list == "y":
            list_todos()

    else:
        print("Invalid choice. Please enter y, n, or exit.")