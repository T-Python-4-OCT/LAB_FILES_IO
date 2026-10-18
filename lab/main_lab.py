import os
print("="*50)
print("Welcome to the To-Do List Program!")
print("="*50)

while True:
    user_input = input("Do you want to add a to-do item? (y/n) : ").strip().lower()
    
    if user_input == "y":
        user_list = input("Enter your to-do item: ")
        
       
        with open("to_do.txt", "a", encoding="utf-8") as file:
            file.write(user_list + "\n")
            
        print("Your to-do item has been saved.")
        
        while True:
            see_items = input("Do you want to see your to-do list? (y/n) : ").strip().lower()
            
            if see_items == "y":
                print("+" * 50)
                print("Your to-do items are:")
                
                with open("to_do.txt", "r", encoding="utf-8") as file:
                    content = file.read()
                    print(content, end="")
                print("+" * 50)
                break  

            elif see_items == "n":
                break  
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
                
    elif user_input == "n":
        delete_choice = input("Do you want to delete your to-do list before exiting? (y/n) : ").strip().lower()
        
        if delete_choice == "y":
            if os.path.exists("to_do.txt"):
                os.remove("to_do.txt")  
                print("Your to-do list has been deleted.")
            elif delete_choice == "n":
                print("Your to-do list has not been deleted.")
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")