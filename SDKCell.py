from tkinter import *
import re
import pdb

class SDKCell:
    def __init__(self, content):
        self.finalNumber = content
        self.entryBox = ""
        self.possibilities = list(range(1,10))
        self.isSolved = False;
        self.coords = []

    def validate_input_value(self):
        input = self.entryBox.get()

    def assign_value_from_input_box(self):
        #if input provided, ensure 0-9
        input = self.entryBox.get()
        matchObj = re.match(r'[0123456789]',str(input))
        if input != "":
            if matchObj:
                self.isSolved = True
                self.possibilities = input
                self.finalNumber = input
                return True
            else:
                return False
        else:
            return True

    def populate_start_value(self,value):
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

    def solve(self):
        solution = str(self.possibilities[0])
        self.isSolved = True
        self.finalNumber = solution
        self.possibilities = solution
        self.display_finalNumber()
        #pdb.set_trace()

    def get_cell_coords(self):
        return f'({self.coords[0]},{self.coords[1]})'
