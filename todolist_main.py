import os
import time

def delay():
    time.sleep(1)

def clear():
    os.system("cls")

tasks_dict = {}

def main():
    while True:
        choice_menu = menu()
        if choice_menu == "1":
            add_task()
        elif choice_menu == "2":
            mark_task_complete()
        elif choice_menu == "3":
            show()
        elif choice_menu == "4":
            quit()
            break
        else:
            print("invalid choice")

def menu():
    while True:
        choice_menu = input( """
1 - add task to a list
2 - mark task as complete
3 - view tasks
4 - quit
--------------------------
Enter your choice:
""")
        if choice_menu.isdigit():
            clear()
            return choice_menu if 0 < int(choice_menu) < 5 else \
                print("Enter number between 1-4")
        else:
            print("Enter numbers only ")

def add_task():
    while True:
        add_task = input("please add a task to you list (if you want exit press\
'n')").lower()
        if add_task == "n":    
            clear()    
            break
        else:
            tasks_dict[add_task] = False

def mark_task_complete():
    show()
    while True:
        choice_complete = input("Enter name of task to mark as complete press \
'n' for back to main menu:\n>> ")
        if choice_complete == 'n':
            show()
            break
        else:
            if choice_complete in tasks_dict:
                tasks_dict[choice_complete] = True
                print(f"The {choice_complete} Task Done")
        
def show():
    for number, task in enumerate(tasks_dict):
        if tasks_dict[task] == False:
            print(f" {number +1} - {task} ❌")
        else:
            print(f" {number +1} - {task} ✔")

def quit():
    for i in range(5):
        print(f"Closing program {'.' *i}")
        delay()
        clear()
            
            
run = main()
 