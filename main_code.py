# TODO Create a function that asks the user what action they want to do. (Main Menu)
import json
import sys


def main_menu():
    print(f"""
    Welcome to TaskManagerApp
    This program will let you create, edit and delete tasks. These task will have a title, a deadline and more...
    To start select the action you want to do!
    Actions:
        1. Create a new task
        2. Modify an existing task
        3. Delete a task
        4. Help/Information
        5. Quit program
""")
    try:
        user_action_choice = input("Enter the corresponding number here: ")
        action_choices = ["1", "2", "3", "4", "5"]
        for i in action_choices:
            if i == user_action_choice:
                post_action_redirect(user_action_choice)
    except ValueError:
        sys.exit("That is not a valid answer. Please try again!")

# TODO Create a function that serves as a redirect to the correct action function.

def post_action_redirect(x: str):
    if x == "1":
        create()
    elif x == "2":
        modify()
    elif x == "3":
        delete()
    elif x == "4":
        information()
    else:
        sys.exit("Program terminated.")


# TODO Create a function that creates a new file and saves it automatically to JSON

def create():
    print("")  # This part of the code will allow the user to create a new file. This file will be saved as a JSON file
    new_file_name = input("What name do you want for your new file? Enter here: ")
    print("Below this line you will be asked for information on the task you want to create.")
    task_name = input("Enter a name for you task: ")
    task_desc = input("Enter a short description of your task: ")
    task_dealine = input("Enter a deadline for your task. Write it in this format: mmddyyyy. Enter here: ")
    task_status = "active"
    task_dict = {
        "Task Name": task_name,
        "Task Description": task_desc,
        "Task Deadline": task_dealine,
        "Task Status": task_status
    }
    with open(f"{new_file_name}.txt", "w") as file:
        file.write(str(task_dict))
    main_menu()



# TODO Create a function that allows the user to modify a task file

def modify():
    print("To delete, add, or modify a task inside your file enter the file name below.")
    file_name = input("Enter here: ")
    with open(f"{file_name}.txt", "r") as file:
        print(file.read())
    print(f"""
    Please enter a number corresponding to the action you want to do:
    
    1. Add new task
    2. Edit existing task
    3. Delete an existing task
    4. Go back to main menu
""")
    user_modify_choice = input("Enter here: ")
    modify_choice_ls = ["1", "2", "3", "4"]
    for i in modify_choice_ls:
        if i == user_modify_choice:
            modify_action_redirect(user_modify_choice, file_name)

def modify_action_redirect(choice, file_name):
    if choice == "1":
        add_new_task(file_name)
    elif choice == "2":
        edit_task(file_name)
    elif choice == "3":
        del_task(file_name)
    else:
        main_menu()

def add_new_task(x):
    with open(f"{x}.txt", "a") as file:









# TODO Create a function that allows the user to delete a specific task
# TODO Create a system that allows the user to view the tasks they have saved in a JSON file
main_menu()

