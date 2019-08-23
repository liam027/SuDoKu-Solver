import re
from tkinter import *
import types

class SDKCell:
    """This object represents a single cell in the SuDoKu puzzle grid"""

    def __init__(self, content):
        self.finalNumber = content
        self.entryBox = "" #the entry widget that represents this cell in UI
        self.possibilities = list(range(1,10))
        self.isSolved = False;
        self.x = "" #coord
        self.y = "" #coord
        """each cell is aware of the cumulative possiblities of it's neighbours, by row, column and box"""
        self.row_neighbour_possibilities = []
        self.column_neighbour_possibilities = []
        self.box_neighbour_possibilities = []

    def assign_value_from_input_box(self):
        #get input from entry widget, validate it and assign to cell properties
        input = self.entryBox.get()
        matchObj = re.match(r'\A[0123456789]',str(input))
        if input != "":
            if matchObj and len(input) == 1:
                self.solve(input)
                return True
            else:
                return False
        else:
            return True

    def load(self,value):
        """load a cell starting value"""
        self.entryBox.delete(0,END)
        self.entryBox.insert(0,value)
        if value != "":
            self.entryBox.config(fg="blue", state="disabled", disabledforeground="blue")

    def solve(self, result = 0):
        """solve a cell and display the result"""
        if result == 0:
            solution = str(self.possibilities[0])
        else:
            solution = str(result)
        self.isSolved = True
        self.finalNumber = solution
        self.possibilities = [0] #use a zero to represent poss. of solved cells
        self.entryBox.delete(0,END)
        self.entryBox.insert(0,self.finalNumber)

    def clear(self):
        """clear this cell's properties (refresh to clean slate)"""
        self.entryBox.config(fg="black", state="normal")
        self.entryBox.delete(0,END)
        self.entryBox.insert(0,"")
        self.finalNumber = ""
        self.possibilities = list(range(1,10))
        self.isSolved = False;
        self.row_neighbour_possibilities = []
        self.column_neighbour_possibilities = []
        self.box_neighbour_possibilities = []

    def display_coords_as_string(self):
        return f'({self.coords[0]},{self.coords[1]})'
