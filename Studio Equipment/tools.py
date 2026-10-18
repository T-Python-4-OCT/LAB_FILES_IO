
def read_number(message):
    #keep asking until the user types a number
    while True:
        text = input(message)
        if text.isdigit():
            return int(text)
        print("Please enter a number")


def find_equipment(data, equipment_id):
    for item in data["equipment"]:
        if item["id"] == equipment_id:
            return item
    return None


def find_transaction(data, transaction_id):
    for transaction in data["transactions"]:
        if transaction["id"] == transaction_id:
            return transaction
    return None


def get_borrowed(data, equipment_id):
    #borrowed = sum of quantities in transactions that are still "borrowed"
    borrowed = 0
    for transaction in data["transactions"]:
        if transaction["equipment_id"] == equipment_id and transaction["status"] == "borrowed":
            borrowed = borrowed + transaction["quantity"]
    return borrowed


def show_equipment(data, item):
    borrowed = get_borrowed(data, item["id"])
    print("")
    print("ID:", item["id"], "-", item["name"], "(" + item["category"] + ")")
    print("Total:", item["quantity"])
    print("Borrowed:", borrowed)
    print("Available:", item["quantity"] - borrowed)
