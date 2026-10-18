def initialize_file():
    """Create the file if it does not exist."""
    file = open("to_do.txt", "a", encoding="utf-8")
    file.close()


def add_task(task):
    """Add a new task."""

    task = task.strip()

    if task == "":
        print("Task cannot be empty.")
        return

    with open("to_do.txt", "a", encoding="utf-8") as file:
        file.write(task + "\n")

    print("Task added successfully.")


def display_tasks():
    """Display all tasks."""

    with open("to_do.txt", "r", encoding="utf-8") as file:
        tasks = file.readlines()

    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n========================")
    print("        TO-DO LIST")
    print("========================")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.strip()}")


def delete_task(task_number):
    """Delete a task by its number."""

    with open("to_do.txt", "r", encoding="utf-8") as file:
        tasks = file.readlines()

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return

    del tasks[task_number - 1]

    with open("to_do.txt", "w", encoding="utf-8") as file:
        file.writelines(tasks)

    print("Task deleted successfully.")