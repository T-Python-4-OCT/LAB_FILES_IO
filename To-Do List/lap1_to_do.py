FILE_NAME = 'to_do.txt'

while True:
    answer = input('Do you want to add a new To-Do item? (yes/no): ').strip().lower()

    if answer == 'exit':
        print('thank you for using the To-Do program, come back again soon')
        break

    if answer == 'yes':
        item = input('Type in your new To-Do item: ').strip()

        if item == '':
            print('Empty item, nothing was saved.')
        else:
            with open(FILE_NAME, 'a', encoding='utf-8') as file:
                file.write(item + '\n')
            print('Item saved.')

    elif answer == 'no':
        answer = input('Do you want to list your To-Do items? (yes/no): ').strip().lower()

        if answer == 'exit':
            print('thank you for using the To-Do program, come back again soon')
            break

        if answer == 'yes':
            try:
                with open(FILE_NAME, 'r', encoding='utf-8') as file:
                    items = file.read().splitlines()
            except FileNotFoundError:
                items = []

            if len(items) == 0:
                print('Your To-Do list is empty.')
            else:
                for item in items:
                    print(item)

    else:
        print("Please answer with 'yes' or 'n' (or type 'exit').")

#MohammedAlnsafi