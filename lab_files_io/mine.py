while True:
    users = input("Do you want to add a new To-Do item? (y/n) or type exit: ")

    if users == "exit":
        print("Thank you for using the To-Do program, come back again soon")
        break
    elif users == "y":
        Wrfile = input("Enter the To-Do item: ")

        with open("to_do.txt", "a", encoding="utf-8") as file:
            file.write(Wrfile + "\n")

    elif users == "n":
        ask = input("Do you want to list your To-Do items? (y/n): ")

        if ask == "y":
             with open("to_do.txt", "r", encoding="utf-8") as file:
                 print(file.read())
            
        elif ask == "n":
            break