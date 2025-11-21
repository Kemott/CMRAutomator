from tkinter import *
from tkinter import ttk
import view.panedWindows.tabPanedWindow as tabPanedWindow

class TabsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(column=0, row=0, sticky=(N,W,E,S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        tabPanedWindow.TabPanedWindow(self)
