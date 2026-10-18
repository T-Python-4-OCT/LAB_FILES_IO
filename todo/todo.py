import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "to_do.txt")

while True:
    choice = input("Do you want to add a new To-Do item? (answer by 'y' for yes, 'n' for no, or 'exit' to quit): ").strip().lower()
    
    if choice == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break
        
    elif choice == "y":
        todo_item = input("Type in your new To-Do item: ")
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(todo_item + "\n")
        print("✓ Added successfully!\n")
        
    elif choice == "n":
        list_choice = input("Do you want to list your To-Do items? answer 'y' for yes and 'n' for no: ").strip().lower()
        
        if list_choice == "y":
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    print("\n--- Your To-Do List ---")
                    for line in file:
                        print(line.strip())
                    print("-----------------------\n")
            except FileNotFoundError:
                print("\n[!] No To-Do items found yet (file doesn't exist).\n")
                
        elif list_choice == "n":
            print("")
        else:
            print("Invalid choice for listing. Please enter 'y' or 'n'.\n")
            
    else:
        print("Invalid input. Please enter 'y', 'n', or 'exit'.\n")