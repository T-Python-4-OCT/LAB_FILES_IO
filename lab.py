FILE = "to_do.txt"


def ask(prompt):
    answer = input(prompt).strip()
    if answer.lower() == "exit":
        return None
    return answer


def add_item(item):
    with open(FILE, "a", encoding="utf-8") as file:
        file.write(item + "\n")


def read_items():
    try:
        with open(FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []


def main():
    while True:
        answer = ask('Do you want to add a new To-Do item? (y/n, or "exit"): ')
        if answer is None:
            break
        answer = answer.lower()

        if answer == "y":
            item = ask("Type your new To-Do item: ")
            if item is None:
                break
            if item:
                add_item(item)
                print("Saved.")
            else:
                print("Empty item, nothing saved.")
        elif answer == "n":
            answer = ask("Do you want to list your To-Do items? (y/n): ")
            if answer is None:
                break
            if answer.lower() == "y":
                items = read_items()
                if items:
                    for item in items:
                        print(item)
                else:
                    print("Your To-Do list is empty.")
        else:
            print('Please answer "y" or "n" (or "exit").')

    print("thank you for using the To-Do program, come back again soon")


main()