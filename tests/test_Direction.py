from model.Direction import Direction

class TestDirection:
    def test_init(self):
        direction = Direction("Direction 30", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION30", 30)
        assert direction.id == 30
        assert direction.name == "Direction 30"
        assert direction.receiver == ["Test1", "Test2", "Test3"]
        assert direction.unloading == "Test1, Test2, Test3"
        assert direction.fileName == "DIRECTION30"
        
    def test_init_with_category(self):
        direction = Direction("Direction 30", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION30", 30, "CATEGORY1")
        assert direction.id == 30
        assert direction.name == "Direction 30"
        assert direction.receiver == ["Test1", "Test2", "Test3"]
        assert direction.unloading == "Test1, Test2, Test3"
        assert direction.fileName == "DIRECTION30"
        assert direction.category == "CATEGORY1"
    
    def test_to_string_without_category(self):
        direction = Direction("Direction 30", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION30", 30)
        assert str(direction) == "30 Direction 30 Test1 Test2 Test3 Test1, Test2, Test3 DIRECTION30"

    def test_to_string_with_category(self):
        direction = Direction("Direction 30", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION30", 30, "CATEGORY1")
        assert str(direction) == "30 Direction 30 Test1 Test2 Test3 Test1, Test2, Test3 DIRECTION30 CATEGORY1"   

    def test_equal_with_category(self):
        direction1 = Direction("Direction 30", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION30", 30, "CATEGORY1")
        direction2 = Direction("Direction 30", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION30", 30, "CATEGORY1")
        assert direction1 == direction2

    def test_equal_without_category(self):
        direction1 = Direction("Direction 30", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION30", 30)
        direction2 = Direction("Direction 30", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION30", 30)
        assert direction1 == direction2

    def test_uneqal_with_different_category(self):
        direction1 = Direction("Direction 30", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION30", 30, "CATEGORY1")
        direction2 = Direction("Direction 30", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION30", 30, "CATEGORY2")
        assert direction1 != direction2

    def test_dict_without_id_or_category(self):
        direction = Direction("Direction Test", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION_TEST")
        assert vars(direction) == { 
            "id" : 0,
            "name": "Direction Test",
            "receiver": ["Test1", "Test2", "Test3"],
            "unloading": "Test1, Test2, Test3",
            "fileName": "DIRECTION_TEST",
            "category": ""
        }
    
    def test_dict_with_id(self):
        direction = Direction("Direction Test", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION_TEST", id=30)
        assert vars(direction) == { 
            "id" : 30,
            "name": "Direction Test",
            "receiver": ["Test1", "Test2", "Test3"],
            "unloading": "Test1, Test2, Test3",
            "fileName": "DIRECTION_TEST",
            "category": ""
        }
    
    def test_dict_with_id_and_category(self):
        direction = Direction("Direction Test", ["Test1", "Test2", "Test3"], "Test1, Test2, Test3", "DIRECTION_TEST", id=30, category="Category 1")
        assert vars(direction) == { 
            "id" : 30,
            "name": "Direction Test",
            "receiver": ["Test1", "Test2", "Test3"],
            "unloading": "Test1, Test2, Test3",
            "fileName": "DIRECTION_TEST",
            "category": "Category 1"
        }