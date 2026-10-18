FILE_NAME = 'to_do.txt'

while True:
    answer = input('Do you want to add a new To-Do item? (y/n or exit): ').strip().lower()

    if answer == 'exit':
        break
    elif answer == 'y':
        item = input('Enter your new To-Do item: ').strip()
        if item:
            with open(FILE_NAME, 'a', encoding='utf-8') as file:
                file.write(item + '\n')
            print('To-Do item saved!')
        else:
            print('Item cannot be empty.')
    elif answer == 'n':
        show = input('Do you want to list your To-Do items? (y/n or exit): ').strip().lower()
        if show == 'exit':
            break
        elif show == 'y':
            try:
                with open(FILE_NAME, 'r', encoding='utf-8') as file:
                    items = file.readlines()
                if items:
                    for item in items:
                        print(item.strip())
                else:
                    print('Your To-Do list is empty.')
            except FileNotFoundError:
                print('Your To-Do list is empty.')
        elif show != 'n':
            print('Invalid choice.')
    else:
        print('Invalid choice.')

print('thank you for using the To-Do program, come back again soon')
