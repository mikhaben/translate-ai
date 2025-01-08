import json

def readJsonFile(file_path) -> dict:
    with open(file_path, 'r') as file:
        return json.load(file)

def writeJsonFile(file_path, data: dict) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
