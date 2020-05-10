import json


class JsonFileOperator:

    @staticmethod
    def read(path):
        with open(path, 'r') as file:
            data = json.load(file)
        return data
