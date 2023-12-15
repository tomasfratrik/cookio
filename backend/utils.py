import json
import datetime

def load_json_file(filename :str):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def write_json_file(filename: str, data: dict):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def recipe_exists(data: dict, name: str):
    for recipe_class in data:
        if recipe_class['class_name'] == name:
            return True
    return False

def get_timestamp():
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{date}"

def get_instance(data: dict, _id: str):
    for recipe_class in data:
        for instance in recipe_class['instances']:
            if instance['id'] == _id:
                return instance
    return None

def get_class(data: dict, _id: str):
    for recipe_class in data:
        if recipe_class['id'] == _id:
            return recipe_class
    return None