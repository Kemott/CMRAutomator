class Direction():
    lastId = 0

    def __init__(self, id):
        self.mainDirection = ""
        self.subDirection = ""

        if id == 0:
            self.id = Direction.lastId + 1
            Direction.lastId += 1
        else:
            self.id = id

    def getName(self):
        if self.name == "":
            self.name = self.mainDirection
            if self.subDirection != "":
                self.name += "_" + self.subDirection
        
        return self.name