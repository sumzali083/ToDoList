#Step 3: Load & Save Functions
#import json
import json
import os
#from asyncio import tasks

#Create a function to load tasks from tasks.json.
#Use Python’s json module (json.load) to read it.
#If the file is empty or missing, return an empty list [].
file = "tasks.json"
def load_tasks():
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return []

#Create a function to save tasks back to tasks.json.
#Use json.dump to write the updated list of dictionaries.
def save_tasks(tasks):
    with open(file, "w") as f:
        json.dump(tasks, f)

#Step 4: Show Menu Options
#Inside a loop (while True), display choices:
#1. View tasks
#2. Add a task
#3. Mark a task as done
#4. Remove a task
#5. Exit
#Ask the user to input a number (input()), and use if/elif to decide what action to run.

def main():
    tasks = load_tasks()
    while True:
        print("\nWould you like to view tasks press 1?")
        print("\nWould you like to add tasks press 2?")
        print("\nWould you like to mark a task as done press 3?")
        print("\nWould you like to remove a task press 4?")
        print("\nWould you like to exit press 5")

        choice = input("select an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Enter task: ")
            tasks = add_task(tasks,task)
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        else:
            print("invalid choice")

#Step 5: View Tasks
#Loop through the list of dictionaries.
#Show the task number, task text, and status.
#Example:
#1. [ ] Buy groceries
#2. [✔] Finish homework
#Tip: Use "✔" for True and " " for False.
def view_tasks(tasks):
    if not tasks:
        print("no tasks saved")
        return #indent
    for i, task in enumerate(tasks, start=1):
        status = "✔" if done == true else status = " "
        print(f"{status} {task['title']}")

#Step 6: Add a Task
#Ask the user for a task description (input()).
#Create a dictionary:
#{"task": user_input, "done": False}
#Append it to the list.
#Call your save function so it’s written to tasks.json.

def add_task(tasks, task):
    tasks.append({"task":task,"done":False})
    save_tasks(tasks)
    return print(f"Task {task} added.")


