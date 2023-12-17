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
        utils.write_json_file('db.json', db)
        return jsonify(instance)

@app.route('/instance/<_id>/ingredients', methods=['DELETE', 'GET', 'POST'])
def ingrediet(_id):
    db = utils.load_json_file('db.json')
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
        instance['name'] = instance['timestamp'] 
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
        recipe_class['desc'] = data['class_desc']
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


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
