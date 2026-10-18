while True:
    ask_user=input("Do you want to add a new To-Do item (Y or N) 'Exit'?").lower()

    if ask_user =="exit":
        break
    elif ask_user=="y":
        todo= input("Enter your new To-do item: ")
        file= open('to_do.txt',"a",encoding="UTF-8")
        file.write(todo+"\n")
        file.close()

        print("To-Do item added successfully!")
    elif ask_user=="n":
        ask_user=input("Do you want to list your To-Do items? (y or n): ").lower()
        try:
            if ask_user == "y":
                file = open("to_do.txt", "r", encoding="UTF-8")
                file.seek(0)
                print(file.read())
                file.close()
        except FileNotFoundError:
            print(" there is no to-do")

    elif ask_user=="n":
        continue

    else:
        print("invalid input")

print("Thank you for using the To-Do program, come back again soon")