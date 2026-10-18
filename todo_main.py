from todo.manager import (
    initialize_file,
    add_task,
    display_tasks,
    delete_task
)


initialize_file()


while True:
    print("\n========================")
    print("       TO-DO MENU")
    print("========================")
    print("1. Add task")
    print("2. Display tasks")
    print("3. Delete task")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number only.")
        continue


    if choice == 1:
        task = input("Enter your task: ")
        add_task(task)


    elif choice == 2:
        display_tasks()


    elif choice == 3:
        display_tasks()

        try:
            task_number = int(input("Enter task number to delete: "))
        except ValueError:
            print("Please enter a number only.")
            continue

        delete_task(task_number)


    elif choice == 4:
        print("Program ended.")
        break


    else:
        print("Invalid choice.")