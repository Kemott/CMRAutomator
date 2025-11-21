from tkinter import *
import view.frames.mainFrame as frame

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("CMR Manager")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.addFrame()
        # self.addMenu()

    def addFrame(self):
        frame.MainFrame(self)

    def addMenu():
        pass
