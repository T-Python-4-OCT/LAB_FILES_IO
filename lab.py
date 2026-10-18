
while True:
    answer = input(
        "Do you want to add a new To-Do item? (y/n) "
    )

    if answer.lower() == "exit":
        print("Thank you for using the To-Do program, come back again soon")
        break

    elif answer.lower() == "y":
        todo = input("Enter your new To-Do item: ")

        with open("to_do.txt", "a") as file:
            file.write(todo + "\n")

        print("To-Do item added successfully!")

    elif answer.lower() == "n":
        read_answer = input(
            "Do you want to list your To-Do items? (y/n) "
        )

        if read_answer.lower() == "y":
            try:
                with open("to_do.txt", "r") as file:
                    print("\nYour To-Do List:")

                    for item in file:
                        print(item.strip())

            except FileNotFoundError:
                print("No To-Do items found.")

        elif read_answer.lower() == "n":
            print("Returning to the main menu...")

        else:
            print("Invalid answer. Please enter y or n.")

    else:
        print("Invalid answer. Please enter y, n, or exit.")