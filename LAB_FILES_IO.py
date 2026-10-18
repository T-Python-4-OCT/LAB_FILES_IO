while True:
    answer = input('Do you want to add a new To-Do item? answer "y" or "n" (or "exit"): ')

    if answer == "exit":
        break

    if answer == "y":
        item = input("Type in your new To-Do item: ")
        #"a" adds the item at the end of the file, on a new line
        with open("to_do.txt", "a", encoding="UTF-8") as file:
            file.write(item + "\n")
        print("Your item was saved")

    elif answer == "n":
        answer = input('Do you want to list your To-Do items? answer "y" or "n" (or "exit"): ')

        if answer == "exit":
            break

        if answer == "y":
            #"a+" creates the file if it does not exist, then seek(0) goes to the start to read
            with open("to_do.txt", "a+", encoding="UTF-8") as file:
                file.seek(0)
                print("Your To-Do items are:")
                print(file.read())

    else:
        print('Please answer "y", "n" or "exit"')

print("thank you for using the To-Do program, come back again soon")
