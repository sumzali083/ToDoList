📝 To-Do List CLI App

A simple command-line To-Do List application built in Python.
You can add tasks, view them, mark them as done, remove them, and save everything to a JSON file.

🚀 Features

View tasks with completion status (✔ for done, [ ] for not done).

Add new tasks.

Mark tasks as completed.

Remove tasks.

Saves all tasks to tasks.json so they persist between runs.

When you run the app, you’ll see a menu like this:

Would you like to view tasks press 1?
Would you like to add tasks press 2?
Would you like to mark a task as done press 3?
Would you like to remove a task press 4?
Would you like to exit press 5

Example session:
select an option: 2
Enter task: Finish coding
Task 'Finish coding' added.

select an option: 1
1. [ ] Finish coding

💾 Data Format

Tasks are stored in tasks.json in this format:

[
  {"task": "Buy groceries", "done": false},
  {"task": "Finish homework", "done": true}
]

✨ Future Improvements

Add due dates to tasks.

Sort tasks (incomplete first).

Allow editing existing tasks.
<img width="1751" height="869" alt="Screenshot 2025-08-24 224255" src="https://github.com/user-attachments/assets/6e2068af-487b-4c20-b27f-c3b983b7dcfc" />
<img width<img width="1715" height="864" alt="Screenshot 2025-08-24 224351" src="https://github.com/user-attachments/assets/ae43b125-3df7-4f1e-9992-4771e2195414" />
="1632" height="857" alt="Screenshot 2025-08-24 224318" src="https://github.com/user-attachments/assets/c9f13e5f-05f8-476a-82fe-299d4e906<img width="1723" height="869" alt="Screenshot 2025-08-24 224341" src="https://github.com/user-attachments/assets/f6a3732f-5f9b-4a53-a2d0-b951e289184e" />
967" />



Add categories/tags.
