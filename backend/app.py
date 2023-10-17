from flask import Flask, jsonify, request
from flask_cors import CORS
import json

# instantiate the app
app = Flask(__name__)
# app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
# CORS(app)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify('pong!')

@app.route('/createrecipe', methods=['POST'])
def create_recipe():
    data = request.get_json()
    new_recipe = {
        'name': data.get('name'),
        'desc': data.get('desc'),
    }
    with open('db.json', 'r') as f:
        json_data = json.load(f)
        json_data.append(new_recipe)
        
    with open('db.json', 'w') as f:
        json.dump(json_data, f, indent=2)

    return jsonify('success')

@app.route('/recipes', methods=['GET'])
def home():
    f = open('db.json')
    data = json.load(f)
    f.close()
    return data


if __name__ == '__main__':
    app.run()