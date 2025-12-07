import model.Direction as dire
import pandas as pd
import pathlib
import json

class DirectionController():
    file = str(pathlib.Path().absolute()/"dataFiles"/"directions.json")
    directions = []

    @staticmethod
    def getAll():
        df = pd.read_json(DirectionController.file)
        print(df.to_dict())

    @staticmethod
    def get(id):
        pass
    
    @staticmethod
    def add(direction):
        pass

    @staticmethod
    def update(direction):
        pass

    @staticmethod
    def delete(direction):
        pass