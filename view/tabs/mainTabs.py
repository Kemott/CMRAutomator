from tkinter import *
from tkinter import ttk
import view.frames.tabsFrame as frame

class MainTabs(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.addTabs()

    def addTabs(self):
        toBeCompletedFrame = frame.TabsFrame(self)
        completedFrame = frame.TabsFrame(self)
        archiveFrame = frame.TabsFrame(self)

        self.add(toBeCompletedFrame, text="Dane do uzupełnienia")
        self.add(completedFrame, text="Dane uzupełnione")
        self.add(archiveFrame, text="Archiwum")
        
