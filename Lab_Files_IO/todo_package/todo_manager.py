def add_todo():
    todo = input("Enter your To-Do item: ")

    with open("to_do.txt", "a+", encoding="utf-8") as file:
        file.write(todo + "\n")

    print("To-Do item added successfully!")


def list_todos():
    with open("to_do.txt", "a+", encoding="utf-8") as file:
        file.seek(0)
        todos = file.read()

    if todos:
        print("\nYour To-Do List:")
        print(todos, end="")
    else:
        print("No To-Do items found.")