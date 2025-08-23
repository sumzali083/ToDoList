

#Step 3: Load & Save Functions
#Create a function to load tasks from tasks.json.
#Use Python’s json module (json.load) to read it.
#If the file is empty or missing, return an empty list [].
#Create a function to save tasks back to tasks.json.
#Use json.dump to write the updated list of dictionaries.
import json

# parse x:
file = "tasks.json"

# the result is a Python dictionary:
print(file)