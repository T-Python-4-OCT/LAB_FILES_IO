while True:
    answer = input("Do you want to add a new To-Do item? (y/n) or type exit: ")

    if answer == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break

    if answer == "y":
        todo = input("Enter your new To-Do item: ")

        with open("to_do.txt", "a") as file:
            file.write(todo + "\n")
    elif answer == "n":
        show_list = input("Do you want to list your To-Do items? (y/n): ")

        if show_list == "y":
            with open("to_do.txt", "r") as file:
                print(file.read())
                