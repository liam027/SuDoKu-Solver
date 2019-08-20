from tkinter import *
import re
import types
import pdb

class SDKCell:
    def __init__(self, content):
        self.finalNumber = content
        self.entryBox = ""
        self.possibilities = list(range(1,10))
        self.isSolved = False;
        self.x = ""
        self.y = ""
        self.row_neighbour_possibilities = []
        self.column_neighbour_possibilities = []
        self.box_neighbour_possibilities = []

    def validate_input_value(self):
        input = self.entryBox.get()

    def assign_value_from_input_box(self):
        #if input provided, ensure 0-9
        input = self.entryBox.get()
        matchObj = re.match(r'[0123456789]',str(input))
        if input != "":
            if matchObj:
                self.solve(input)
                return True
            else:
                return False
        else:
            return True

    def load(self,value):
        self.entryBox.delete(0,END)
        self.entryBox.insert(0,value)
        if value != "":
            self.entryBox.config(fg="blue", state="disabled", disabledforeground="blue")

    def solve(self, result = 0):
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
        self.finalNumber = ""
        self.possibilities = list(range(1,10))
        self.isSolved = False;
        self.row_neighbour_possibilities = []
        self.column_neighbour_possibilities = []
        self.box_neighbour_possibilities = []
        self.entryBox.config(fg="black", state="normal")

    def display_coords_as_string(self):
        return f'({self.coords[0]},{self.coords[1]})'
