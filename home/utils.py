import json


def get_data():
    with open('names.json') as data:
        names = json.load(data)

    return names
