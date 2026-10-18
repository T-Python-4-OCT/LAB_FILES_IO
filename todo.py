from pathlib import Path

TODO_FILE = Path(__file__).with_name("to_do.txt")

def add_todo_item():
    item = input("Type your new To-Do item: ").strip()
    if not item:
        print("The To-Do item cannot be empty.")
        return

    with TODO_FILE.open("a", encoding="UTF-8") as file:
        file.write(item + "\n")
    print("To-Do item saved.")


def list_todo_items():
    if not TODO_FILE.exists():
        print("Your To-Do list is empty.")
        return

    with TODO_FILE.open("r", encoding="UTF-8") as file:
        items = [line.rstrip("\n") for line in file]

    if not items:
        print("Your To-Do list is empty.")
        return

    print("Your To-Do items:")
    for item in items:
        print(item)