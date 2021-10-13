import json

def read_source(filename: str) -> str:
    source_code = ""
    with open(filename, 'r') as file:
        source_code = file.read()
    return source_code

def write_to_json(AST: dict, filename: str) -> None:
    with open(filename, 'w') as file:
        json.dump(AST, file, indent = 4)

def read_json(filename) -> dict:
    with open(filename, 'r') as file:
        return json.load(file)