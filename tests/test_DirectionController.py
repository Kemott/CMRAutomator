import pathlib
from model.Direction import Direction
from controller.DirectionController import DirectionController
import pytest
import shutil
import os
from validation.Exceptions import IdDontExistsException
from validation.Exceptions import IdAlreadeyExistsException
from validation.Exceptions import NotProperIdException

class TestDirectionController:
    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        self.initialization()
        yield
        self.cleaning()

    def initialization(self):
        self.dataFile = str(pathlib.Path().absolute()/"tests"/"directions.json")
        self.tempFile = str(pathlib.Path().absolute()/"tests"/"temp.json")
        shutil.copyfile(self.dataFile, self.tempFile)
        DirectionController.file = self.tempFile

    def cleaning(self):
        if os.path.exists(self.tempFile):
            os.remove(self.tempFile)

    def test_get_all_types_matches(self, subtests):
        allDirections = DirectionController.getAll()
        for direction in allDirections:
            with subtests.test(msg="Type test", i=direction):
                assert type(direction) == Direction

    def test_get_all_number_of_items_matches(self):
        allDirections = DirectionController.getAll()
        assert len(allDirections) == 29

    def test_get_existing_id(self):
        assert DirectionController.get(13).id == 13
    
    def test_get_id_bigger_than_existing_number(self):
        with pytest.raises(IdDontExistsException):
            DirectionController.get(30)
    
    def test_get_id_0(self):
        with pytest.raises(IdDontExistsException):
            DirectionController.get(0)

    def test_add_proper_Direction(self):
        direction = Direction("Direction 30", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION30")
        assert DirectionController.add(direction) == 30
        assert DirectionController.get(30) == direction

    def test_add_existing_id_Direction(self):
        direction = Direction("Direction 13", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION13", 13)
        with pytest.raises(IdAlreadeyExistsException):
            DirectionController.add(direction)

    def test_add_proper_with_id_Direction(self):
        direction = Direction("Direction 30", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION30", 30)
        assert DirectionController.add(direction) == 30
        assert DirectionController.get(30) == direction

    def test_add_not_next_id_Direction(self):
        direction = Direction("Direction 30", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION30", 31)
        with pytest.raises(NotProperIdException):
            DirectionController.add(direction)
    
    def test_add_with_category(self):
        direction = Direction("Direction 30", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION30", 30, "Direction1")
        assert DirectionController.add(direction) == 30