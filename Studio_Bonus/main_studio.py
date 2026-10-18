"""Start here: python main_studio.py"""
from studio.storage import load_data
from studio.operations import (
    add_equipment, view_equipment, search_equipment, update_equipment,
    delete_equipment, borrow_equipment, return_equipment, view_history,
)
# from studio.operations import * (ودي استخدمها بس خوفك تسوي لي تعارض بين اسماء الفنكشنز فا اريح لي استدعي كل وحدة )


def main():
    try:
        data = load_data()
    except (OSError, ValueError) as error:
        print(f'Cannot open studio data: {error}')
        return

    options = {
        '1': add_equipment,
        '2': view_equipment,
        '3': search_equipment,
        '4': update_equipment,
        '5': delete_equipment,
        '6': borrow_equipment,
        '7': return_equipment,
        '8': view_history,
    }
    while True:
        print('''\n=================================
    STUDIO EQUIPMENT MANAGER
=================================
1. Add Equipment
2. View All Equipment
3. Search Equipment
4. Update Equipment
5. Delete Equipment
6. Borrow Equipment
7. Return Equipment
8. View Borrowing History
9. Exit\n''')
        choice = input('Select an option: ').strip()
        if choice == '9':
            print('Thank you for using Studio Equipment Manager!')
            break
        action = options.get(choice)
        if action:
            try:
                action(data)
            except OSError as error:
                print(f'File save failed: {error}')
                return
        else:
            print('Invalid option. Please choose 1-9.')


if __name__ == '__main__':
    main()
