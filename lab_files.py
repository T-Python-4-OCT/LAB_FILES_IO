FILE_NAME = "to_do.txt"


def add_item():
    item = input("Type in your new To-Do item: ").strip()
    if item == "":
        print("The item cannot be empty.")
        return
    with open(FILE_NAME, "a") as file:
        file.write(item + "\n")
    print("Item saved.")


def list_items():
    try:
        with open(FILE_NAME, "r") as file:
            items = [line.strip() for line in file if line.strip() != ""]
    except FileNotFoundError:
        items = []

    if not items:
        print("Your To-Do list is empty.")
        return

    print("Your To-Do items:")
    for item in items:
        print(item)


def main():
    while True:
        answer = input('Do you want to add a new To-Do item? (y/n, or "exit" to quit): ').strip().lower()

        if answer == "exit":
            break
        elif answer == "y":
            add_item()
        elif answer == "n":
            answer = input('Do you want to list your To-Do items? (y/n, or "exit" to quit): ').strip().lower()
            if answer == "exit":
                break
            elif answer == "y":
                list_items()
            elif answer != "n":
                print("Please answer with y or n.")
        else:
            print("Please answer with y or n.")

    print("thank you for using the To-Do program, come back again soon")


main()