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
def home():
    f = open('db.json')
    data = json.load(f)
    f.close()
    return data


if __name__ == '__main__':
    app.run()