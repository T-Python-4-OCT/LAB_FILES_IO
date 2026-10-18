while True:
    answer = input("Do you want to add a new To-Do item? (y/n/exit): ").lower()

    if answer == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break

    elif answer == "y":
        item = input("Type your new To-Do item: ")

        with open("to_do.txt", "a") as f:
            f.write(item + "\n")

    elif answer == "n":
        show = input("Do you want to list your To-Do items? (y/n): ").lower()

        if show == "y":
            try:
                with open("to_do.txt", "r") as f:
                    for line in f:
                        print(line.strip())

            except FileNotFoundError:
                print("No items yet.")

        elif show == "n":
            continue

        else:
            print("Invalid answer. Please enter y or n.")

    else:
        print("Invalid answer. Please enter y, n, or exit.")