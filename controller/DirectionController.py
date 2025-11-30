import model.Direction as dire
import pandas as pd
import pathlib

class DirectionController():
    file = str(pathlib.Path().absolute()/"dataFiles"/"directions.csv")
    directions = []

    @staticmethod
    def getAll():
        df = pd.read_csv(DirectionController.file, sep=";")
        DirectionController.directions = []
        df = df.reset_index()
        for index, row in df.iterrows():
            direction = dire.Direction(row['Id'])
            DirectionController.directions.append(direction)

        for direction in DirectionController.directions:
            print(direction)

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