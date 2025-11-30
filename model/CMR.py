class CMR():
    def __init__(self, name=""):
        if name != "":
            self.name = name
        
        self.car = ""
        self.trailer = ""
        self.containers = []
        self.direction = ""
        self.contentsLines = []
        self.carrierLines = []
        self.carriersCommentsLines = []

    def createName(self):
        self.name = self.direction
        self.name += "_"

        if len(self.containers) != 0:
            for container in self.containers:
                self.name += container
                if self.containers[len(self.containers)-1] != container:
                    self.name += "_"
        else:
            self.name += self.trailer
    
    def getListText(self):
        return self.name