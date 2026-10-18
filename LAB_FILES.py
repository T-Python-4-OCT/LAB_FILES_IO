"""A simple file-based to-do list."""

from pathlib import Path


DATA_DIRECTORY = Path(__file__).resolve().parent
TODO_FILE = DATA_DIRECTORY / "to_do.txt"


# ---------------------------------------------------------------------------
# To-do list
# ---------------------------------------------------------------------------

def run_todo_list():
    """Add and display to-do items until the user enters exit."""
    print("\nTo-Do List (type 'exit' at any prompt to quit)")
    while True:
        answer = input("Do you want to add a new To-Do item? (y/n): ").strip().lower()
        if answer == "exit":
            break
        if answer == "y":
            item = input("Type your new To-Do item: ").strip()
            if item.lower() == "exit":
                break
            if item:
                with TODO_FILE.open("a", encoding="utf-8") as todo_file:
                    todo_file.write(item + "\n")
                print("To-Do item saved.")
            else:
                print("An empty item was not saved.")
        elif answer == "n":
            answer = input("Do you want to list your To-Do items? (y/n): ").strip().lower()
            if answer == "exit":
                break
            if answer == "y":
                if TODO_FILE.exists():
                    print("\nYour To-Do items:")
                    with TODO_FILE.open("r", encoding="utf-8") as todo_file:
                        items = [line.rstrip("\n") for line in todo_file]
                    if items:
                        for item in items:
                            print(item)
                    else:
                        print("(No items yet.)")
                else:
                    print("(No items yet.)")
            elif answer != "n":
                print("Please answer 'y' or 'n'.")
        else:
            print("Please answer 'y' or 'n', or type 'exit'.")

    print("Thank you for using the To-Do program, come back again soon")


# ---------------------------------------------------------------------------

def main():
    run_todo_list()


if __name__ == "__main__":
    main()
