while True:

    answer = input("Do you want to add a new To-Do item? (y/n) or type 'exit': ")

    if answer == "exit":
        print("Thank you for using the To-Do program, come back again soon")
        break

    elif answer == "y":
        item = input("Enter your To-Do item: ")

        with open("to_do.txt", "a", encoding="utf-8") as file:
            file.write(item + "\n")

    elif answer == "n":
        answer = input("Do you want to list your To-Do items? (y/n): ")

        if answer == "y":
            try:
                with open("to_do.txt", "r", encoding="utf-8") as file:
                    for item in file:
                        print(item.strip())

            except FileNotFoundError:
                print("No To-Do items found.")

        elif answer == "n":
            continue