def read_positive_int(prompt):
    text = input(prompt).strip()
    if text.isascii() and text.isdigit() and int(text) > 0:
        return int(text)
    print("Please enter a whole number greater than 0.")
    return None


def read_text(prompt):
    text = input(prompt).strip()
    if text == "":
        print("This field cannot be empty.")
        return None
    return text


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


def borrowed_count(data, equipment_id):
    total = 0
    for transaction in data["transactions"]:
        if transaction["equipment_id"] == equipment_id and transaction["status"] == "borrowed":
            total += transaction["quantity"]
    return total


def available_count(data, item):
    return item["quantity"] - borrowed_count(data, item["id"])