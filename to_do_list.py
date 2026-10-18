def add_task (task_name):
    # task_name = str(input("enter the new task :"))
    file = open("tasks.txt","a",encoding="utf-8")
    file.write(task_name + "\n")
    file.close()
    print("the task is added successfuly")
def show_task():
    try:
        file= open("tasks.txt","r",encoding="utf-8")
        tasks=file.read()
        file.close
        if tasks:
            print(tasks)
        else:
            print("there is no tasks now please one")

    except FileNotFoundError:
        print("the tasks file is not found please add new one.")


def delete_task(task_to_remove):
    file= open("tasks.txt","r",encoding="utf-8")
    lins= file.readlines()
    file.close()
    save_task= []
    for task in lins:
        if task_to_remove not in task:
            save_task.append(task)
    file = open("tasks.txt","w",encoding="utf-8")
    file.writelines(save_task)
    file.close
    print("the task is deleted")
while True:
    user_choise = input("Do you want to add a new To-Do item? (y/n/exit): ")
    
    if user_choise =="exit":
        print("thank you for uding to do proggram come back soon")
        break
    elif user_choise == "y":
        add_task (input("enter the new task :"))
    elif user_choise == "n":
        print("do you want to see your to do list? (y/n)")
        user_input=input()
        if user_input == "y":
            show_task()



