"""Functions for equipment CRUD and checkout/returns."""
from datetime import date
from .storage import save_data


def ask_positive_number(message):
    try:
        number = int(input(message))
        if number > 0:
            return number
    except ValueError:
        pass
    print('Please enter a positive whole number.')
    return None


def find_equipment(data, equipment_id):
    return next((item for item in data['equipment'] if item['id'] == equipment_id), None)


def borrowed_count(data, equipment_id):
    return sum(t['quantity'] for t in data['transactions']
               if t['equipment_id'] == equipment_id and t['status'] == 'borrowed')


def next_id(records):
    return max((record['id'] for record in records), default=0) + 1


def add_equipment(data):
    name = input('Equipment name: ').strip()
    category = input('Category: ').strip()
    quantity = ask_positive_number('Total quantity: ')
    if not name or not category or quantity is None:
        print('Invalid equipment information.')
        return
    item = {'id': next_id(data['equipment']), 'name': name,
            'category': category, 'quantity': quantity}
    # Also consider IDs in old transactions so deleted IDs are not reused.
    item['id'] = max(item['id'], max((t['equipment_id'] for t in data['transactions']), default=0) + 1)
    data['equipment'].append(item)
    save_data(data)
    print(f"Equipment added! ID: {item['id']}")


def show_equipment(item, data):
    borrowed = borrowed_count(data, item['id'])
    print(f"\nID: {item['id']} | {item['name']} | Category: {item['category']}")
    print(f"Total: {item['quantity']} | Borrowed: {borrowed} | Available: {item['quantity'] - borrowed}")


def view_equipment(data):
    if not data['equipment']:
        print('No equipment found.')
    for item in data['equipment']:
        show_equipment(item, data)


def search_equipment(data):
    word = input('Search name or category: ').strip().lower()
    matches = [item for item in data['equipment']
               if word in item['name'].lower() or word in item['category'].lower()]
    if not matches:
        print('No matching equipment found.')
    for item in matches:
        show_equipment(item, data)


def update_equipment(data):
    equipment_id = ask_positive_number('Equipment ID: ')
    item = find_equipment(data, equipment_id) if equipment_id is not None else None
    if not item:
        print('Equipment not found.')
        return
    print('Press Enter to keep the current value.')
    name = input(f"Name [{item['name']}]: ").strip()
    category = input(f"Category [{item['category']}]: ").strip()
    quantity_text = input(f"Total quantity [{item['quantity']}]: ").strip()
    quantity = item['quantity']
    if quantity_text:
        try:
            quantity = int(quantity_text)
        except ValueError:
            print('Quantity must be a whole number. No changes saved.')
            return
    if quantity < borrowed_count(data, item['id']) or quantity <= 0:
        print('Total quantity must be positive and cannot be less than borrowed units.')
        return
    item.update({'name': name or item['name'], 'category': category or item['category'], 'quantity': quantity})
    save_data(data)
    print('Equipment updated.')


def delete_equipment(data):
    equipment_id = ask_positive_number('Equipment ID to delete: ')
    item = find_equipment(data, equipment_id) if equipment_id is not None else None
    if not item:
        print('Equipment not found.')
    elif borrowed_count(data, equipment_id):
        print('Cannot delete: some units are currently borrowed.')
    else:
        data['equipment'].remove(item)
        save_data(data)
        print('Equipment deleted. Borrowing history is kept.')


def borrow_equipment(data):
    employee = input('Employee name: ').strip()
    equipment_id = ask_positive_number('Equipment ID: ')
    quantity = ask_positive_number('Quantity to borrow: ')
    if not employee or equipment_id is None or quantity is None:
        print('Invalid borrowing request.')
        return
    item = find_equipment(data, equipment_id)
    if not item:
        print('Equipment not found.')
        return
    available = item['quantity'] - borrowed_count(data, equipment_id)
    if quantity > available:
        print(f'Borrowing rejected. Only {available} available.')
        return
    transaction = {'id': next_id(data['transactions']), 'equipment_id': equipment_id,
                   'employee': employee, 'quantity': quantity,
                   'date': date.today().isoformat(), 'status': 'borrowed'}
    data['transactions'].append(transaction)
    save_data(data)
    print(f"Borrowed successfully! Transaction ID: {transaction['id']}; Available: {available - quantity}")


def return_equipment(data):
    transaction_id = ask_positive_number('Transaction ID: ')
    transaction = next((t for t in data['transactions'] if t['id'] == transaction_id), None)
    if not transaction:
        print('Transaction not found.')
    elif transaction['status'] == 'returned':
        print('Already returned. Availability is unchanged.')
    else:
        transaction['status'] = 'returned'
        save_data(data)
        print('Equipment returned successfully.')


def view_history(data):
    if not data['transactions']:
        print('No borrowing history yet.')
    for t in data['transactions']:
        print(f"Transaction #{t['id']} | Employee: {t['employee']} | Equipment ID: {t['equipment_id']} "
              f"| Quantity: {t['quantity']} | Date: {t['date']} | Status: {t['status']}")
