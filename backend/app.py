import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

# local
# from utils import load_json_file
import utils

app = Flask(__name__)
CORS(app)

# test server enpoint
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify('pong!')

@app.route('/instance/<_id>', methods=['DELETE', 'GET', 'POST', 'PUT'])
def instance(_id):
    db = utils.load_json_file('db.json')
    if request.method == 'GET':
        instance = utils.get_instance(db, _id)
        if instance is None:
            return jsonify('error')

        return jsonify(instance) 
    elif request.method == 'DELETE':
        instances = utils.remove_instance(_id)
        return jsonify(instances)
    elif request.method == 'PUT':
        data = request.get_json()
        instance = utils.get_instance(db, _id)
        if instance is None:
            return jsonify('error')
        instance['name'] = data['name']
        instance['desc'] = data['desc']
        instance['rating'] = data['rating']
        instance['pinned'] = data['pinned']
        instance['ingredients'] = data['ingredients']
        utils.write_json_file('db.json', db)
        return jsonify(instance)

@app.route('/instance/<_id>/ingredients', methods=['DELETE', 'GET', 'POST', 'PUT'])
def ingrediet(_id):
    db = utils.load_json_file('db.json')
    if request.method == 'GET':
        instance = utils.get_instance(db, _id)
        if instance is None:
            return jsonify('error')

        return jsonify(instance['ingredients'])
    if request.method == 'POST':
        ingredient = request.get_json()
        instance = utils.get_instance(db, _id)
        if instance is None:
            return jsonify('error')
        instance['ingredients'].append(ingredient)
        utils.write_json_file('db.json', db)
        return jsonify(instance['ingredients'])
    elif request.method == 'DELETE':
        ingredient = request.get_json()
        instance = utils.get_instance(db, _id)
        if instance is None:
            return jsonify('error')
        instance['ingredients'].remove(ingredient)
        utils.write_json_file('db.json', db)
        return jsonify(instance['ingredients'])
    elif request.method == 'PUT':
        ingredient = request.get_json()
        instance = utils.get_instance(db, _id)
        if instance is None:
            return jsonify('error')
        for ingredient_to_remove in instance['ingredients']:
            if ingredient['name'] == ingredient_to_remove['name']:
                index = instance['ingredients'].index(ingredient_to_remove)
                instance['ingredients'][index] = ingredient
                break
        utils.write_json_file('db.json', db)
        return jsonify(instance['ingredients'])

@app.route('/instance/pinned', methods=['GET','POST', 'PUT'])
def instance_pinned():
    db = utils.load_json_file('db.json')
    if request.method == 'GET':
        # get all pinned instances
        pinned_instances = []
        for recipe_class in db:
            for instance in recipe_class['instances']:
                if instance['pinned']:
                    pinned_instances.append(instance)
        return jsonify(pinned_instances)


@app.route('/recipe_classes', methods=['GET','POST'])
def recipe_classes():
    if request.method == 'POST':
        existing_data = utils.load_json_file('db.json')
        data = request.get_json()
        recipe_class_name = data['class_name']
        exists = utils.recipe_exists(existing_data, recipe_class_name)

        instance = {}
        instance['id'] = str(uuid.uuid4())
        instance['timestamp'] = utils.get_timestamp()
        instance['name'] = recipe_class_name
        instance['desc'] = ""
        instance['rating'] = -1
        instance['pinned'] = False
        instance['ingredients'] = []

        if exists:
            for recipe_class in existing_data:
                if recipe_class['class_name'] == recipe_class_name:
                    recipe_class['instances'].append(instance)
                    utils.write_json_file('db.json', existing_data)
                    return jsonify(instance)
        else:
            data['id'] = str(uuid.uuid4())
            instances = []
            instances.append(instance)
            data['instances'] = instances
            existing_data.append(data)
            utils.write_json_file('db.json', existing_data)
            return jsonify(instance)

    data = utils.load_json_file('db.json')
    return jsonify(data)

@app.route('/recipe_classes/<_id>/instances', methods=['DELETE', 'GET','POST'])
def recipe_classes_instances(_id):
    db = utils.load_json_file('db.json')
    if request.method == 'GET':
        recipe_class = utils.get_class(db, _id)
        if recipe_class is None:
            return jsonify('error')
        return jsonify(recipe_class['instances'])

@app.route('/recipe_classes/<_id>', methods=['DELETE', 'GET','POST', 'PUT'])
def recipe_class_detail(_id):
    db = utils.load_json_file('db.json')
    if request.method == 'GET':
        recipe_class = utils.get_class(db, _id)
        if recipe_class is None:
            return jsonify('error')
        return jsonify(recipe_class)
    elif request.method == 'PUT':
        data = request.get_json()
        recipe_class = utils.get_class(db, _id)
        if recipe_class is None:
            return jsonify('error')
        recipe_class['class_name'] = data['class_name']
        recipe_class['class_desc'] = data['class_desc']
        utils.write_json_file('db.json', db)
        return jsonify(recipe_class)

@app.route('/recipes/<_id>', methods=['DELETE', 'GET','POST'])
def delete_recipe_class(_id):
    db = utils.load_json_file('db.json')
    if request.method == 'DELETE':
        recipe_class = utils.get_class(db, _id)
        if recipe_class is None:
            print('error')
            return jsonify('error')
        db.remove(recipe_class)
        utils.write_json_file('db.json', db)
        return jsonify(db)
    elif request.method == 'GET':
        recipe_class = utils.get_class(db, _id)
        if recipe_class is None:
            return jsonify('error')
        return jsonify(recipe_class)

@app.route('/recipes', methods=['GET'])
def recipes():
    data = jsonify('error')
    if request.method == 'GET':
        with open('db.json') as f:
            data = json.load(f)
        return jsonify(data)
    return data

@app.route('/ingredients', methods=['GET', 'POST'])
def ingredients():
    unique_ingredients = utils.get_unique_ingredients()
    return jsonify(unique_ingredients)

@app.route('/groups', methods=['GET', 'POST', 'DELETE', 'PUT'])
def groups():
    groups_db = utils.get_all_groups()
    print("here")
    if request.method == 'GET':
        return jsonify(groups_db)
    elif request.method == 'POST':
        data = request.get_json()
        group_name = data['name']
        exists = utils.get_group_by_name(group_name)
        if exists is not None:
            return jsonify('error')
        group = {}
        group['name'] = group_name
        group['instances'] = []
        groups_db.append(group)
        utils.write_json_file('groups.json', groups_db)
        return jsonify(group)
    elif request.method == 'PUT':
        data = request.get_json()
        old_group_name = data['old_name']
        new_group_name = data['new_name']
        print(f"old group name: {old_group_name}")
        print(f"new group name: {new_group_name}")
        group = utils.get_group_by_name(old_group_name)
        if group is None:
            return jsonify('error')
        # check if new group name already exists
        exists = utils.get_group_by_name(new_group_name)
        if exists is not None:
            return jsonify('error')
        utils.group_rename(old_group_name, new_group_name)
        return jsonify(group)

@app.route('/groups/<_name>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def groups_group(_name):
    groups_db = utils.get_all_groups()
    if request.method == 'DELETE':
        # print("here-delete")
        # data = request.get_json()
        # print("here-getting data")
        group_name = _name
        print(f"deleting group {group_name}")
        group = utils.get_group_by_name(group_name)
        if group is None:
            return jsonify('error')
        groups_db.remove(group)
        utils.write_json_file('groups.json', groups_db)
        return jsonify(groups_db)


@app.route('/group/<_name>', methods=['GET', 'POST'])
def group(_name):
    if request.method == 'GET':
        group = utils.get_group_by_name(_name)
        if group is not None:
            return jsonify(group)
        else:
            return jsonify('error')

@app.route('/groups/<_name>/meals', methods=['GET', 'POST', 'DELETE', 'PUT'])
def group_meals(_name):
    groups_db = utils.get_all_groups()
    db = utils.load_json_file('db.json')
    if request.method == 'PUT':
        data = request.get_json()
        group_name = _name
        meal_ids = data['meals']
        print(f"meal ids: {meal_ids}")

        # for group in groups_db:
        #     if group['name'] == group_name:
        #         # find those instaces
        #         # append id and name
        #         # dont reset, just append
        #         group['instances'] = []
        group = utils.get_group_by_name(group_name)
        for recipe in db:
            for instance in recipe['instances']:
                if instance['id'] in meal_ids:
                    group = utils.get_group_by_name(group_name)
                    # if it is alreay in the group, dont add it
                    exists = False
                    for sub_instance in group['instances']:
                        if sub_instance['id'] == instance['id']:
                            exists = True
                            break    
                    if exists:
                        continue

                    sub_instance = { 'id': instance['id'], 'name': instance['name'] }
                    utils.add_meal_to_group(group_name, sub_instance)
                    group['instances'].append(sub_instance)


        return jsonify('success')


# @app.route('/group/<_name>/add/<_instance>', methods=['GET', 'POST'])
# def add_instance_to_group(_name, _instance):
#     if request.method == 'POST':
#         group = utils.get_group_by_name(_name)
#         if group is not None:
#             group['instances'].append(_instance)
#             utils.write_json_file('groups.json', group)
#             return jsonify(group)
#         else:
#             return jsonify('error')


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
