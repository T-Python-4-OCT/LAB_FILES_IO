
def ToDoList():

    while True :
            
            UserEnter = input('Do You To Add a New To-Do Item ? (Answer by "Y" for Yes and "N" for No) ').upper()
            
            if UserEnter == 'EXIT' :
                print('THANK YOU, GOOD BYE!')
                break

            elif UserEnter == 'Y':
                ToDo = input('Okay, Enter Your To-Do Item: ')
            
                file = open("to_do.txt", 'a+')
                file.write(f"{ToDo}\n")
                file.close()

            elif UserEnter == 'N' :
                ListToDo = input('Do You Want To List Your To-Do Items? (Y/N) ').upper()
            
                if ListToDo == 'Y' :
                    file = open('to_do.txt','r')
                    print(file.read())
                    file.close() 


