from tkinter import *
from tkinter import ttk
import view.frames.tableFrame as tableFrame
import view.frames.optionsFrame as optionsFrame

class TabPanedWindow(ttk.PanedWindow):
    def __init__(self, parent, data=[]):
        super().__init__(parent, orient="horizontal")
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        self.data = data
        self.addFrames()

    def addFrames(self):
        f1 = tableFrame.TableFrame(self, data=self.data)
        f2 = optionsFrame.OptionsFrame(self)
        self.add(f1, weight=1)
        self.add(f2, weight=0)

