from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
# app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

# test server enpoint
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify('pong!')

@app.route('/recipes', methods=['GET'])
def recipes():
    data = jsonify('error')
    if request.method == 'GET':
        with open('db.json') as f:
            data = json.load(f)
        return jsonify(data)
    return data


if __name__ == '__main__':
    app.run()