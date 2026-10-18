# Equipment
import json
import os

def add_equipment():
    if not os.path.exists("studio_data.json"):
        data = {"equipment": [], "transactions": []}
        with open("studio_data.json", "r") as file:
            json.dump(data, file, indent=4)

    with open("studio_data.json", "r") as file:
        data = json.load(file)

    name = input("Enter equipment name: ")
    category =  input("Enter equipment category: ")
    quantity =  input("Enter equipment quantity: ")

    if data["equipment"]:
        new_id = max(item["id"] for item in data["equipment"]) + 1
    else:
        new_id = 1


    equipment = {
        "id": new_id,
        "name": name,
        "category": category,
        "quantity": quantity
    }

    data["equipment"].append(equipment)

    with open("studio_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("equipment added successfully!")
    print(f"equipment ID: {new_id}")    


def view_equipment():
    
    if not os.path.exists("studio_data.json"):
        print("No equipment data found.")
        return

    with open("studio_data.json", "r") as file:
            data = json.load(file)

    equipment_list = data["equipment"]

    if not equipment_list:
        print("No equipment available.")
        return

    print("\n--- All Studio Equipment ---")


    for item in equipment_list:
        print(f"ID: {item['id']}") 
        print(f"Name: {item['name']}") 
        print(f"Category: {item['category']}") 
        print(f"Total quantity: {item['quantity']}") 
        print("-"*30) 
    


def search_equipment():

    if not os.path.exists("studio_data.json"):
        print("No equipment data found.")
        return
    
    with open("studio_data.json", "r") as file:
        data = json.load(file)
    
    equipment_list = data["equipment"]
    
    if not equipment_list:
        print("No equipment available.")
        return
    

    search_name = input("Enter equipment name of category to search: ").strip().lower()

    found = False

    for item in equipment_list:
        if (search_name in item["name"].lower()
            or search_name in item["category"].lower()):

            print("\n--- Equipment Found ---")
            print(f"ID: {item['id']}") 
            print(f"Name: {item['name']}") 
            print(f"Category: {item['category']}") 
            print(f"Total quantity: {item['quantity']}") 
            print("-"*30)

            found = True


    if not found:
        print("No matching equipment found.")



def update_equipment():
    with open("studio_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    equipment_list = data["equipment"]

    equipment_id = input("Enter equipment ID to update: ")

    for equipment in equipment_list:
        if str(equipment["id"]) == equipment_id:
            print("\n Current equipment information:")
            print(f"Name: {equipment['name']}") 
            print(f"Category: {equipment['category']}") 
            print(f"Quantity: {equipment['quantity']}")

            new_name = input("Enter new name (press Enter to keep current): ")
            new_category = input("Enter new category (press Enter to keep current): ")
            new_quantity = input("Enter new quantity (press Enter to keep current): ")

            if new_name.strip():
                equipment["name"] = new_name.strip()

            if new_category.strip():
                equipment["category"] = new_category.strip()

            if new_quantity.strip():
                try:
                    quantity = int(new_quantity)

                    if quantity <0:
                        print("Quantity cannot be negative.")
                        return
                    equipment["quantity"] = quantity
                except ValueError:
                    print("Invalid quantity. Please Enter a number.")

            with open("studio_data.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("Equipment updated successfully!")
            return
    print("Equipment ID not found.")





def delete_equipment():
    with open("studio_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    equipment_list = data["equipment"]

    equipment_id = input("Enter equipment ID to delete: ").strip()

    for equipment in equipment_list:
        if str(equipment["id"]) == equipment_id:
            print("\n Equipment Found:")
            print(f"ID: {equipment['id']}")
            print(f"Name: {equipment['name']}") 
            print(f"Category: {equipment['category']}") 
            print(f"Quantity: {equipment['quantity']}")

            confirm = input("Are you sure want to deleted this equipment? (y/n): ").strip().lower()

            if confirm == "y":
                equipment_list.remove(equipment)
                with open("studio_data.json", "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
                print("Equipment deleted successfully!")

            elif confirm == "n":
                print("Deletion cancelled.")

            else:
                print("Invalid choice. Please enter y or n.")

            return

    print("Equipment ID not found.")




