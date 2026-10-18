#

while True:
    answer = input('Do you want to add a new To-Do item? (y/n) or type "exit": ')

    if answer.lower() == "exit":
        print("Thank you for using the To-Do program, come back again soon")
        break

    elif answer.lower() == "y":
        todo = input("Enter your new To-Do item: ")

        with open("to_do.txt", "a+") as file:
            file.write(todo + "\n")



    elif answer.lower() == "n":
        read_answer = input("Do you want to list your To-Do items? (y/n): ")

        if read_answer.lower() == "y":
                with open("to_do.txt", "a+") as file:
                    file.seek(0)
                    print(file.read())


    else:
        print("Please enter 'y', 'n', or 'exit' ")
