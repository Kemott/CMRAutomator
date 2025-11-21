from tkinter import *
from tkinter import ttk

class TableFrame(ttk.Labelframe):
    def __init__(self, parent):
        super().__init__(parent, text='Lista', width=500, height=100)
        self.grid(column=0, row=0, sticky=(N,W,E,S))
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        

        
