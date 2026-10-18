from storage import save_data


def return_equipment(data):
    transaction_id = input("Enter transaction ID: ")

    for transaction in data["transactions"]:

        if str(transaction["id"]) == transaction_id:

            if transaction["status"] == "returned":
                print("This equipment has already been returned.")
                return

            transaction["status"] = "returned"

            save_data(data)

            print("Equipment returned successfully!")
            print("Transaction ID:", transaction["id"])
            return

    print("Transaction ID not found.")