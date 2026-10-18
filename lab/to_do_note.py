
from pathlib import Path

file_path = Path(__file__).resolve().parent / "to_do.txt"

while True:
    choice = input("Add a new To-Do item? (y/n/exit): ").strip().lower()

    if choice == "exit":
        break

    if choice == "y":
        task = input("Enter your To-Do item (or exit): ").strip()

        if task.lower() == "exit":
            break

        if not task:
            print("Task cannot be empty.")
            continue

        with open(file_path, "a", encoding="utf-8") as file:
            file.write(task + "\n")

        print("Task added successfully.")

    elif choice == "n":
        show_tasks = input("List your To-Do items? (y/n/exit): ").strip().lower()

        if show_tasks == "exit":
            break

        if show_tasks == "y":
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    tasks = file.readlines()

                if not tasks:
                    print("Your To-Do list is empty.")
                else:
                    print("\nYour To-Do list:")
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task.strip()}")

            except FileNotFoundError:
                print("Your To-Do list is empty.")

        elif show_tasks != "n":
            print("Please enter y, n, or exit.")

    else:
        print("Please enter y, n, or exit.")

print("Thank you for using the To-Do program, come back again soon.")
