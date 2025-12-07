from tkinter import *
from tkinter import ttk
import controller.DirectionController as directionController

for direction in directionController.DirectionController.getAll():
    print(direction)