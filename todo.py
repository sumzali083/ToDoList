#Step 3: Load & Save Functions
#Create a function to load tasks from tasks.json.
#Use Python’s json module (json.load) to read it.
#If the file is empty or missing, return an empty list [].
#Create a function to save tasks back to tasks.json.
#Use json.dump to write the updated list of dictionaries.
#import json

import json

file = "tasks.json"

with open(file) as json_file:
    data = json.load(json_file)     # data is a dict with "tasks" inside
    tasks = data["tasks"]           # now tasks is a list of dicts
    for i in tasks:
        task_name = i["task"]
        status_data = i["done"]
        print(f"{task_name} is {status_data}")
