#Step 3: Load & Save Functions
#Create a function to save tasks back to tasks.json.
#Use json.dump to write the updated list of dictionaries.
#import json
import json
import os

#Create a function to load tasks from tasks.json.
#Use Python’s json module (json.load) to read it.
#If the file is empty or missing, return an empty list [].
file = "tasks.json"
def load_tasks():
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return []

