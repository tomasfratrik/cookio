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

def remove_instance(_id: str):
    db = load_json_file('db.json')
    for recipe_class in db:
        for instance in recipe_class['instances']:
            if instance['id'] == _id:
                recipe_class['instances'].remove(instance)
                write_json_file('db.json', db)
                return recipe_class['instances']
    return None

def get_unique_ingredients():
    db = load_json_file('db.json')
    ingredients = set()
    for recipe_class in db:
        for instance in recipe_class['instances']:
            for ingredient in instance['ingredients']:
                ingredients.add(ingredient["name"].lower())
    ingredients = list(ingredients)
    return ingredients

def get_all_groups():
    groups_db = load_json_file('groups.json')
    return groups_db

def get_group_by_name(name: str):
    groups_db = load_json_file('groups.json')
    for group in groups_db:
        if group['name'].upper() == name.upper():
            return group
    return None

def get_group_instances(name: str):
    groups_db = load_json_file('groups.json')
    db = load_json_file('db.json')

def group_rename(name: str, new_name: str):
    groups_db = load_json_file('groups.json')
    for group in groups_db:
        if group['name'].upper() == name.upper():
            group['name'] = new_name
            write_json_file('groups.json', groups_db)
            return group
    return None

def add_meal_to_group(group_name: str, meal: str):
    groups_db = load_json_file('groups.json')
    for group in groups_db:
        if group['name'].upper() == group_name.upper():
            group['instances'].append(meal)
            write_json_file('groups.json', groups_db)
            return group
    return None



