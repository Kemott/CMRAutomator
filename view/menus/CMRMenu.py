from tkinter import *

class CMRMenu(Menu):
    def __init__(self, parent):
        super().__init__(parent)
        self.add_command(label="Utwórz nowy dokument", command=self.newDocument)

    def newDocument(self):
        print("You must still program this!")