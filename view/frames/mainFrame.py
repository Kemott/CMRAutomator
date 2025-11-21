from tkinter import *
from tkinter import ttk
import view.tabs.mainTabs as mainTabs

class MainFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.addTabs()

    def addTabs(self):
        tabs = mainTabs.MainTabs(self)
        
