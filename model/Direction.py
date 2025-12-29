class Direction():
    def __init__(self, name, receiver, unloading, fileName, id = 0, category = ""):
        self.category = category
        
        self.id = id
        self.name = name
        self.receiver = receiver
        self.unloading = unloading
        self.fileName = fileName

        print(self)

    def __str__(self):
        result = str(self.id) + " "
        result += self.name + " "
        for line in self.receiver:
            result += line + " "
        
        result += self.unloading + " "
        result += self.fileName

        if self.category != "":
            result += " " + self.category

        return result
    
    def __eq__(self, other):
        if self.id == other.id and self.name == other.name and self.receiver == other.receiver and self.unloading == other.unloading and self.fileName == other.fileName and self.category == other.category:
            return True
        else:
            return False
        
    def to_save(self):
        result = vars(self)
        if(self.category != ""):
            result.pop('category')
            return {
                "category": self.category,
                "data": result
            }
        else:
            return {
                "category": "",
                "data": result
            }