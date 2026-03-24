import json
import os 

file_name="expenses.json"

"""Load expenses from a JSON file and Retruns an empty list if
the file does not exist or is invalid."""

def load_expenses():
    if not os.path.exists(file_name):
        return []
    try:
        with open(file_name,'r') as file:
            data=json.load(file)
            #will ensure that data is list
            if isinstance(data,list):
                return data
            return[]
    except (json.JSONDecodeError, IOError):
        return []
    
#save expense list to a Json file

def save_expenses(expenses):
    with open(file_name,'w') as file:
        json.dump(expenses,file,indent=4)

        


