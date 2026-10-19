while True:
    answer = input("Do you want to add a new To-Do item? (y/n): ")

    if answer == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break

    elif answer == "y":
        item = input("Enter your new To-Do item: ")

        with open("to_do.txt", "a") as file:
            file.write(item + "\n")

        print("To-Do item added successfully")

    elif answer == "n":
        read = input("Do you want to list your To-Do items? (y/n): ")

        if read == "exit":
            print("thank you for using the To-Do program, come back again soon")
            break

        elif read == "y":
            try:
                with open("to_do.txt", "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("No To-Do items found")

        elif read == "n":
            continue

        else:
            print("Invalid answer")

    else:
        print("Invalid answer")