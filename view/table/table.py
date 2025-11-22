from tkinter import *
from tkinter import ttk

class Table(ttk.Frame):
    def __init__(self, parent, data = []):
        super().__init__(parent)
        self.grid(column=0, row=0, sticky=(N,S,E,W))
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        rowsList = Listbox(self, width=0, height=0)
        rowsList.grid(column=0, row=0, sticky=(N,W,E,S))
        scroll = ttk.Scrollbar(self, orient=VERTICAL, command=rowsList.yview)
        scroll.grid(column=1, row=0, sticky=(N,W,E,S))
        rowsList.configure(yscrollcommand=scroll.set)
        for row in data:
            pass
        
        
