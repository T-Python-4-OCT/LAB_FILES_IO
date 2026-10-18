while True:

    ask = input("do you want to add a new To-Do item ?")

    if ask.lower() == "exit":
        break

    if ask.lower() in ["y", "yes"]:
        print("Type in his new item TO-DO :")
        with open("to_do.txt", "a") as file:
            file.write(input("Write what you want to do:") + "\n")

    elif ask.lower() in ["no", "n"]:
        askk = input("do you want to list your To-Do item ?")
        if askk.lower() in ["yes", "y"]:
            print("this is TO-DO :")
            try:
                with open("to_do.txt", "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("No To-Do items found.")


print("thank you for using the To-Do program, come back again soon")