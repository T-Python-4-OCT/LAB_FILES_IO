from storage import save_data


def delete_equipment(data):
    equipment_id = input("Enter equipment ID to delete: ")

    for item in data["equipment"]:
        if str(item["id"]) == equipment_id:

            borrowed = 0

            for transaction in data["transactions"]:
                if transaction["equipment_id"] == item["id"] and transaction["status"] == "borrowed":
                    borrowed += transaction["quantity"]

            if borrowed > 0:
                print("Cannot delete equipment. Some items are still borrowed.")
                return

            data["equipment"].remove(item)

            save_data(data)

            print("Equipment deleted successfully!")
            return

    print("Equipment ID not found.")