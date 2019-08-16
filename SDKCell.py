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
        self.coords = []
        self.row_neighbour_possibilities = []
        self.column_neighbour_possibilities = []

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
        self.entryBox.config(fg="blue", state="disabled", disabledforeground="blue")

    def display_finalNumber(self):
        if self.isSolved:
            self.entryBox.delete(0,END)
            self.entryBox.insert(0,self.finalNumber)
        else:
            self.entryBox.delete(0,END)
            self.entryBox.insert(0,"")

    def solve(self, result = 0):
        if result == 0:
            solution = str(self.possibilities[0])
        else:
            solution = str(result)
        self.isSolved = True
        self.finalNumber = solution
        self.possibilities = [0] #use a zero to represent poss. of solved cells
        self.display_finalNumber()

    def get_cell_coords(self):
        return f'({self.coords[0]},{self.coords[1]})'

    def flatten_list(self, list_of_lists): #flattens a list of lists into single array
        flat_list = []
        for sublist in list_of_lists:
            if type(sublist) is list: #make sure the item in list_of_lists is a list (iterable)
                for item in sublist:
                    flat_list.append(item)
        flat_list = list(dict.fromkeys(flat_list))
        self.row_neighbour_possibilities = flat_list
