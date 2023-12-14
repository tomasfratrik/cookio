import json

def load_json_file(filename :str):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def write_json_file(filename: str, data: dict):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)