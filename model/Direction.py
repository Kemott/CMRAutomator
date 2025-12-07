class Direction():
    def __init__(self, id, name, receiver, unloading, fileName, category = ""):
        self.category = category
        
        self.id = id
        self.name = name
        self.receiver = receiver
        self.unloading = unloading
        self.fileName = fileName

    def __str__(self):
        result = str(self.id) + " "
        result += self.name + " "
        for line in self.receiver:
            result += line + " "
        
        result += self.unloading + " "
        result += self.fileName + " "

        if self.category != "":
            result += self.category

        return result