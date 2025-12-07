import model.Direction as dire
import pandas as pd
import pathlib

class DirectionController():
    file = str(pathlib.Path().absolute()/"dataFiles"/"directions.json")

    @staticmethod
    def getAll():
        df = pd.read_json(DirectionController.file)
        directions = df['directions']
        result = []
        for direction in directions:
            if "subdirections" in direction:
                for subdirection in direction['subdirections']:
                    result.append(dire.Direction(subdirection["id"], subdirection["direction"], subdirection["receiver"], subdirection["unloading"], subdirection["fileName"], direction["direction"]))
            else:
                result.append(dire.Direction(direction["id"], direction["direction"], direction["receiver"], direction["unloading"], direction["fileName"]))
        
        return result

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