import model.Direction as dire
import pandas as pd
import pathlib
from validation.Exceptions import IdDontExistsException
from validation.Exceptions import IdAlreadeyExistsException
from validation.Exceptions import FileCouldNotBeSavedException


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
                    result.append(dire.Direction(subdirection["direction"], subdirection["receiver"], subdirection["unloading"], subdirection["fileName"], subdirection["id"], direction["direction"]))
            else:
                result.append(dire.Direction(direction["direction"], direction["receiver"], direction["unloading"], direction["fileName"], direction["id"]))
        
        return result

    @staticmethod
    def get(id):
        df = pd.read_json(DirectionController.file)
        directions = df['directions']
        for direction in directions:
            if "subdirections" in direction:
                for subdirection in direction['subdirections']:
                    if subdirection["id"] == id:
                        return dire.Direction(subdirection["direction"], subdirection["receiver"], subdirection["unloading"], subdirection["fileName"], subdirection["id"], direction["direction"])
                    else:
                        continue
            else:
                if direction['id'] == id:
                    return dire.Direction(direction["direction"], direction["receiver"], direction["unloading"], direction["fileName"], direction["id"])
            
        raise IdDontExistsException({"id": id})
    
    @staticmethod
    def add(direction):
        df = pd.read_json(DirectionController.file)

        lastId = df['lastUsedId'][0]
        if direction.id <= lastId and direction.id != 0:
            raise IdAlreadeyExistsException()
        elif direction.id > lastId:
            direction.id = lastId + 1
        
        lastId += 1
        directions = df['directions']
        if direction.category != "":
            for dir in directions:
                if direction.to_save()['category'] == dir["direction"]:
                    subdirections = dir['subdirections']
                    subdirections[len(subdirections) + 1] = direction.to_save()['data']
                    break
        else:
            directions[len(directions) + 1] = direction.to_save()['data']

        try:
            DirectionController.save_to_file(lastId, directions)
        except:
            raise FileCouldNotBeSavedException()
        else:
            return lastId

    @staticmethod
    def update(direction):
        pass

    @staticmethod
    def delete(direction):
        pass

    @staticmethod
    def save_to_file(lastId, directions):
        # We are here, to save the new data to the file
        print(lastId)
        print(directions)