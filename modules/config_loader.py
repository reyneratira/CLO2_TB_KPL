import json

def load_services(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)