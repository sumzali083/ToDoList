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

Add categories/tags.
