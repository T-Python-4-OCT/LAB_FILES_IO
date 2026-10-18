from todo import add_todo_item, list_todo_items

def main():
    while True:
        answer = input(
            'do you want to add a new To-Do item? answer by "y" for yes and "n" for no: '
        ).strip().lower()

        if answer == "exit":
            break
        if answer == "y":
            add_todo_item()
        elif answer == "n":
            list_answer = input(
                'Do you want to list your To-Do items? Enter "y", "n", or "exit": '
            ).strip().lower()

            if list_answer == "exit":
                break
            if list_answer == "y":
                list_todo_items()
            elif list_answer != "n":
                print('Please enter "y", "n", or "exit".')
        else:
            print('Please enter "y", "n", or "exit".')

    print("Thank you for using the To-Do program, come back again soon..")


if __name__ == "__main__":
    main()