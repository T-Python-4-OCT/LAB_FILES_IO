
import json
import os
from datetime import date


def LoadData():
    if os.path.exists('studio_data.json'):
        with open('studio_data.json', 'r') as File:
            Data = json.load(File)
    else:
        Data = {
            'equipment': [],
            'transactions': []
        }
        SaveData(Data)

    return Data


def SaveData(Data):
    with open('studio_data.json', 'w') as File:
        json.dump(Data, File, indent=4)


def GetID(Items):
    if Items:
        return max(Item['id'] for Item in Items) + 1
    return 1


def GetEquipment(Data, EquipmentID):
    for Equipment in Data['equipment']:
        if Equipment['id'] == EquipmentID:
            return Equipment
    return None


def GetTransaction(Data, TransactionID):
    for Transaction in Data['transactions']:
        if Transaction['id'] == TransactionID:
            return Transaction
    return None


def GetBorrowedQty(Data, EquipmentID):
    Qty = 0

    for Transaction in Data['transactions']:
        if (Transaction['equipment_id'] == EquipmentID
                and Transaction['status'] == 'borrowed'):
            Qty += Transaction['quantity']

    return Qty


def AddEquipment(Data):
    EquipmentName = input('Enter The Equipment Name: ').strip()
    EquipmentCategory = input('Enter Equipment Category: ').strip()

    if not EquipmentName or not EquipmentCategory:
        print('Name and category cannot be empty!')
        return

    for Equipment in Data['equipment']:
        if Equipment['name'].lower() == EquipmentName.lower():
            print('Equipment Already Exists!')
            return

    try:
        EquipmentQty = int(input('Enter The Equipment Quantity: '))
        if EquipmentQty <= 0:
            print('Quantity must be greater than zero!')
            return
    except ValueError:
        print('Please enter a valid number!')
        return

    ID = GetID(Data['equipment'])

    NewEquipment = {
        'id': ID,
        'name': EquipmentName,
        'category': EquipmentCategory,
        'quantity': EquipmentQty
    }

    Data['equipment'].append(NewEquipment)
    SaveData(Data)
    print('Equipment Added Successfully!')


def DisplayEquipment(Data):
    if not Data['equipment']:
        print('No Equipment Available')
        return

    for Equipment in Data['equipment']:
        BorrowedQty = GetBorrowedQty(Data, Equipment['id'])
        AvailableQty = Equipment['quantity'] - BorrowedQty

        print(f"\nID: {Equipment['id']}")
        print(f"Name: {Equipment['name']}")
        print(f"Category: {Equipment['category']}")
        print(f"Total Quantity: {Equipment['quantity']}")
        print(f"Borrowed Quantity: {BorrowedQty}")
        print(f"Available Quantity: {AvailableQty}")


def SearchEquipment(Data):
    SearchName = input('Enter Equipment Name or Category: ').strip().lower()
    Found = False

    for Equipment in Data['equipment']:
        if (SearchName in Equipment['name'].lower()
                or SearchName in Equipment['category'].lower()):
            BorrowedQty = GetBorrowedQty(Data, Equipment['id'])
            AvailableQty = Equipment['quantity'] - BorrowedQty

            print(f"\nID: {Equipment['id']}")
            print(f"Name: {Equipment['name']}")
            print(f"Category: {Equipment['category']}")
            print(f"Available Quantity: {AvailableQty}")
            Found = True

    if not Found:
        print('Equipment Not Found!')


def UpdateEquipment(Data):
    DisplayEquipment(Data)

    try:
        EquipmentID = int(input('\nEnter Equipment ID to update: '))
    except ValueError:
        print('Please enter a valid ID!')
        return

    Equipment = GetEquipment(Data, EquipmentID)

    if Equipment is None:
        print('Equipment Not Found!')
        return

    EquipmentName = input('Enter New Name: ').strip()
    EquipmentCategory = input('Enter New Category: ').strip()

    if not EquipmentName or not EquipmentCategory:
        print('Name and category cannot be empty!')
        return

    for OtherEquipment in Data['equipment']:
        if (OtherEquipment['id'] != EquipmentID
                and OtherEquipment['name'].lower() == EquipmentName.lower()):
            print('Equipment Name Already Exists!')
            return

    try:
        EquipmentQty = int(input('Enter New Total Quantity: '))
        if EquipmentQty <= 0:
            print('Quantity must be greater than zero!')
            return
    except ValueError:
        print('Please enter a valid quantity!')
        return

    BorrowedQty = GetBorrowedQty(Data, EquipmentID)

    if EquipmentQty < BorrowedQty:
        print('Quantity cannot be less than the borrowed quantity!')
        return

    Equipment['name'] = EquipmentName
    Equipment['category'] = EquipmentCategory
    Equipment['quantity'] = EquipmentQty

    SaveData(Data)
    print('Equipment Updated Successfully!')


def DeleteEquipment(Data):
    DisplayEquipment(Data)

    try:
        EquipmentID = int(input('\nEnter Equipment ID to delete: '))
    except ValueError:
        print('Please enter a valid ID!')
        return

    Equipment = GetEquipment(Data, EquipmentID)

    if Equipment is None:
        print('Equipment Not Found!')
        return

    if GetBorrowedQty(Data, EquipmentID) > 0:
        print('Cannot delete equipment while it is borrowed!')
        return

    Data['equipment'].remove(Equipment)
    SaveData(Data)
    print('Equipment Deleted Successfully!')


def BorrowEquipment(Data):
    DisplayEquipment(Data)

    try:
        EquipmentID = int(input('\nEnter Equipment ID to borrow: '))
        EquipmentQty = int(input('Enter Quantity to borrow: '))

        if EquipmentQty <= 0:
            print('Quantity must be greater than zero!')
            return
    except ValueError:
        print('Please enter valid numbers!')
        return

    Equipment = GetEquipment(Data, EquipmentID)

    if Equipment is None:
        print('Equipment Not Found!')
        return

    EmployeeName = input('Enter Employee Name: ').strip()

    if not EmployeeName:
        print('Employee name cannot be empty!')
        return

    BorrowedQty = GetBorrowedQty(Data, EquipmentID)
    AvailableQty = Equipment['quantity'] - BorrowedQty

    if EquipmentQty > AvailableQty:
        print(f'Only {AvailableQty} units are available!')
        return

    TransactionID = GetID(Data['transactions'])

    NewTransaction = {
        'id': TransactionID,
        'equipment_id': EquipmentID,
        'employee': EmployeeName,
        'quantity': EquipmentQty,
        'date': date.today().isoformat(),
        'status': 'borrowed'
    }

    Data['transactions'].append(NewTransaction)
    SaveData(Data)

    print(f'Equipment Borrowed Successfully! Transaction ID: {TransactionID}')


def ReturnEquipment(Data):
    try:
        TransactionID = int(input('Enter Transaction ID to return: '))
    except ValueError:
        print('Please enter a valid ID!')
        return

    Transaction = GetTransaction(Data, TransactionID)

    if Transaction is None:
        print('Transaction Not Found!')
        return

    if Transaction['status'] == 'returned':
        print('This equipment has already been returned!')
        return

    Transaction['status'] = 'returned'
    SaveData(Data)

    print('Equipment Returned Successfully!')


def ViewBorrowingHistory(Data):
    if not Data['transactions']:
        print('No Borrowing History Available')
        return

    for Transaction in Data['transactions']:
        Equipment = GetEquipment(Data, Transaction['equipment_id'])

        if Equipment is None:
            EquipmentName = 'Deleted Equipment'
        else:
            EquipmentName = Equipment['name']

        print(f"\nTransaction ID: {Transaction['id']}")
        print(f"Employee: {Transaction['employee']}")
        print(f"Equipment: {EquipmentName}")
        print(f"Equipment ID: {Transaction['equipment_id']}")
        print(f"Quantity: {Transaction['quantity']}")
        print(f"Date: {Transaction['date']}")
        print(f"Status: {Transaction['status']}")


def Main():
    Data = LoadData()

    while True:
        print('\n===== Studio Equipment Checkout System =====')
        print('1. Add Equipment')
        print('2. View All Equipment')
        print('3. Search Equipment')
        print('4. Update Equipment')
        print('5. Delete Equipment')
        print('6. Borrow Equipment')
        print('7. Return Equipment')
        print('8. View Borrowing History')
        print('9. Exit')

        Choice = input('Choose an option: ')

        if Choice == '1':
            AddEquipment(Data)
        elif Choice == '2':
            DisplayEquipment(Data)
        elif Choice == '3':
            SearchEquipment(Data)
        elif Choice == '4':
            UpdateEquipment(Data)
        elif Choice == '5':
            DeleteEquipment(Data)
        elif Choice == '6':
            BorrowEquipment(Data)
        elif Choice == '7':
            ReturnEquipment(Data)
        elif Choice == '8':
            ViewBorrowingHistory(Data)
        elif Choice == '9':
            print('Goodbye!')
            break
        else:
            print('Invalid Choice! Please try again.')


if __name__ == '__main__':
    Main()
