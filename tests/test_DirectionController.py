import pathlib
from model.Direction import Direction
from controller.DirectionController import DirectionController

class TestDirectionController:
    def initialization(self):
        DirectionController.file = str(pathlib.Path().absolute()/"tests"/"directions.json")

    def test_get_all(self):
        self.initialization()
        allDirections = DirectionController.getAll()
        for direction in allDirections:
            assert type(direction) == Direction

        assert len(allDirections) == 29