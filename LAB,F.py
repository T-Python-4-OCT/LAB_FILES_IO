while True:
    choice = input("Do you want to add a new To-Do item? (y/n or exit): ")

    if choice == "exit":
        print("Thank you for using the To-Do program, come back again soon👋")
        break

    if choice == "y":
        todo = input("Enter your To-Do item: ")

        with open("to_do.txt", "a") as file:
            file.write(todo + "\n")

    elif choice == "n":
        choice = input("Do you want to list your To-Do items? (y/n): ")

        if choice == "y":
            with open("to_do.txt", "r") as file:
                print(file.read())

        elif choice == "n":
            continue

