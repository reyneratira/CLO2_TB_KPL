import json

def load_services(filepath) -> dict:
    with open(filepath, 'r') as f:
        return json.load(f)