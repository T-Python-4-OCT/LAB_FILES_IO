FILENAME = "to_do.txt"

while True:
    answer = input('Do you want to add a new To-Do item? (yes/no, or "exit" to quit): ').strip().lower()

    if answer == "exit":
        print("Thank you for using the To-Do program, come back again soon")
        break

    elif answer == "yes":
        item = input("Type in your new To-Do item: ").strip()
        with open(FILENAME, "a") as file:
            file.write(item + "\n")

    elif answer == "no":
        show = input('Do you want to list your To-Do items? (yes/no, or "exit" to quit): ').strip().lower()

        if show == "exit":
            print("Thank you for using the To-Do program, come back again soon")
            break

        elif show == "yes":
            try:
                with open(FILENAME, "r") as file:
                    items = file.readlines()
                if items:
                    print("\nYour To-Do items:")
                    for item in items:
                        print(item.strip())
                    print()
                else:
                    print("Your To-Do list is empty.\n")
            except FileNotFoundError:
                print("Your To-Do list is empty.\n")

    else:
        print('Invalid input. Please type "yes", "no", or "exit".')