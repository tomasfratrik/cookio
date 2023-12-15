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

@app.route('/recipe_classes', methods=['GET','POST'])
def recipe_classes():
    if request.method == 'POST':
        data = request.get_json()
        data['id'] = str(uuid.uuid4())
        existing_data = utils.load_json_file('db.json')
        existing_data.append(data)
        utils.write_json_file('db.json', existing_data)
        return jsonify("ok")

    data = utils.load_json_file('db.json')
    return jsonify(data)

@app.route('/recipes', methods=['GET'])
def recipes():
    data = jsonify('error')
    if request.method == 'GET':
        with open('db.json') as f:
            data = json.load(f)
        return jsonify(data)
    return data


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
