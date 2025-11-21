from tkinter import *
import view.menus.CMRMenu as CMRMenu

class MenuBar(Menu):
    def __init__(self, parent):
        super().__init__(parent)
        menu_cmr = CMRMenu.CMRMenu(self)
        self.add_cascade(menu=menu_cmr, label="CMR")