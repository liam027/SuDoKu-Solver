from tkinter import filedialog
from tkinter import *
from SDKGrid import *
from SDKCell import *

class App:
    def __init__(self, master, **kwargs):
        #generate new SDKgrid for future input value storage
        self.puzzleGrid = SDKGrid("")
        self.targetCell = None
        self.foundStep = False
        #window size, spacer and container for entry elements
        self.master=master
        master.geometry('600x600+0+0')
        topHeader = Frame(width = 600, height = 40)
        topHeader.pack()
        topFrame = Frame( width = 600, height = 600)
        topFrame.pack()

        #create input elements and assign to SDKgrid
        for x in range(9):
            for y in range(9):
                input = Entry(topFrame, width = 2, font = ("Courier", 24), justify="center")
                self.puzzleGrid.get_cell_at_coords(x,y).entryBox = input
                input.grid(row=x,column=y)

        #separate grid and buttons
        gridToButtonSpacer = Frame(width = 600, height = 60)
        gridToButtonSpacer.pack()

        #container for buttons
        bottomFrame = Frame( width = 600, height = 200)
        bottomFrame.pack()

        solveButton = Button(bottomFrame, text = "SOLVE", fg = "blue", command=lambda : self.solve_button())
        solveButton.pack(side=LEFT)

        stepButton = Button(bottomFrame, text = "STEP", fg = "black", command=lambda : self.step_button())
        stepButton.pack(side=LEFT)

        populateButton = Button(bottomFrame, text = "LOAD", fg = "black", command=lambda : self.load())
        populateButton.pack(side=LEFT)

        saveButton = Button(bottomFrame, text = "SAVE", fg = "black", command=lambda : self.save())
        saveButton.pack(side=LEFT)

        quitButton = Button(bottomFrame, text = "QUIT", fg = "red", command=bottomFrame.quit)
        quitButton.pack(side=LEFT)

    def say_hi(self):
        print("hi there, everyone!")

    def step_button(self):
        self.foundStep = False
        if self.puzzleGrid.assign_input_values():
            for i in range(30): #[BUG]  iteration based?
                for x in range(9):
                    for y in range(9):
                        if self.foundStep == False:
                            self.solve_step(x,y)

        if self.isComplete() == True:
            print("Puzzle Completed!")


    def load(self,file = ""):
        if file == "":
            fin = filedialog.askopenfilename(initialdir="puzzles/",title="Select file", filetypes =(("JSON files","*.json"),("All file types","*.*")))
        else:
            fin = file
        self.puzzleGrid.load(fin)

    """def solve_button(self):
        if self.puzzleGrid.assign_input_values():
            for i in range(30): #[BUG] iteration based?
                for x in range(9):
                    for y in range(9):
                        self.solve_full(x,y)
        else:
            print("Inputs not valid!")
        if self.isComplete() == True:
            print("Puzzle Completed!")
        else:
            print("Puzzle NOT Complete!")"""

    def save(self):
        if self.puzzleGrid.assign_input_values():
            fout = filedialog.asksaveasfilename(initialdir="puzzles/",title="Select save location", filetypes =(("JSON files","*.json"),("All file types","*.*")))
            self.puzzleGrid.save(fout)
        else:
            print("Bad input!")

    """def solve_full(self,x,y):
                self.targetCell = self.puzzleGrid.grid[x][y]
                if(self.targetCell.isSolved == False):
                    self.calculate_possibilities()
                    if len(self.targetCell.possibilities) == 1:
                        self.targetCell.solve()
                    else:
                        self.check_neighbours()"""

    def solve_step(self,x,y):
        if(self.foundStep == False):
            self.targetCell = self.puzzleGrid.grid[x][y]
            if(self.targetCell.isSolved == False):
                self.calculate_possibilities(x,y)
                if len(self.targetCell.possibilities) == 1:
                    self.targetCell.solve()
                    self.foundStep = True
                else:
                    self.check_neighbours()

    def calculate_possibilities(self,x,y):
        self.reduce_possibilities_by_row(x,y)
        self.reduce_possibilities_by_column(x,y)
        self.reduce_possibilities_by_box(x,y)

    def check_neighbours(self):
        """if a target's possibility isn't in it's neighbours, the only choice is to assign that value to target cell"""
        for p in self.targetCell.possibilities:
            if p != 0:
                if p not in self.targetCell.row_neighbour_possibilities:
                    self.targetCell.solve(p)
                    self.foundStep = True
                elif p not in self.targetCell.column_neighbour_possibilities:
                    self.targetCell.solve(p)
                    self.foundStep = True
                elif p not in self.targetCell.box_neighbour_possibilities:
                    self.targetCell.solve(p)
                    self.foundStep = True

    def reduce_possibilities_by_row(self,x,y):
        #check for numbers in horizontal adjacent cells and remove those from target's possibilities
        for i in range(1,10): #content
            for n in range(9): #y-coord adjacent cells
                if n != y:
                    self.targetCell.row_neighbour_possibilities.append( self.puzzleGrid.grid[x][n].possibilities)
                if str(i) == self.puzzleGrid.grid[x][n].finalNumber:
                    self.RemovePossiblityFromTargetCell(i,self.targetCell)
        self.targetCell.row_neighbour_possibilities = self.flatten_list(self.targetCell.row_neighbour_possibilities)

    def reduce_possibilities_by_column(self,x,y):
        #check for numbers in vertical adjacent cells and remove those from target's possibilities
        for i in range(1,10): #content
            for n in range(9): #x-coord adjacent cells
                if n != x:
                    self.targetCell.column_neighbour_possibilities.append( self.puzzleGrid.grid[n][y].possibilities)
                if str(i) == self.puzzleGrid.grid[n][y].finalNumber:
                    self.RemovePossiblityFromTargetCell(i,self.targetCell)
        self.targetCell.column_neighbour_possibilities = self.flatten_list(self.targetCell.column_neighbour_possibilities)

    def reduce_possibilities_by_box(self,x,y):
        #check 3x3 box that contains targetCell for numbers and remove them from target possibilities
        if x < 3 and y < 3: #top left
            self.check_box1(x,y)
        if x > 2 and x < 6 and y < 3: #middle left
            self.check_box2(x,y)
        if x > 5 and y < 3: #bottom left
            self.check_box3(x,y)
        if x < 3 and y > 2 and y < 6: #top middle
            self.check_box4(x,y)
        if x > 2 and x < 6 and y > 2 and y < 6: #center
            self.check_box5(x,y)
        if x > 5 and y > 2 and y < 6: #bottom middle
            self.check_box6(x,y)
        if x < 3 and y > 5: #top right
            self.check_box7(x,y)
        if x > 2 and x < 6 and y > 5: #middle right
            self.check_box8(x,y)
        if x > 5 and y > 5: #bottom right
            self.check_box9(x,y)
        self.targetCell.box_neighbour_possibilities = self.flatten_list(self.targetCell.box_neighbour_possibilities)

    def check_box1(self,x,y):  #top left
        for i in range(1,10): #[BUG] could move this below to save time?
            for r in range(0,3):
                for c in range(0,3):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)
    def check_box2(self,x,y): #middle left
        for i in range(1,10):
            for r in range(3,6):
                for c in range(0,3):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)
    def check_box3(self,x,y): #bottom left
        for i in range(1,10):
            for r in range(6,9):
                for c in range(0,3):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)
    def check_box4(self,x,y): #top middle
        for i in range(1,10):
            for r in range(0,3):
                for c in range(3,6):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)
    def check_box5(self,x,y): #center
        for i in range(1,10):
            for r in range(3,6):
                for c in range(3,6):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)
    def check_box6(self,x,y): #bottom middle
        for i in range(1,10):
            for r in range(6,9):
                for c in range(3,6):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)
    def check_box7(self,x,y): #top right
        for i in range(1,10):
            for r in range(0,3):
                for c in range(6,9):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)
    def check_box8(self,x,y): #middle right
        for i in range(1,10):
            for r in range(3,6):
                for c in range(6,9):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)
    def check_box9(self,x,y): #bottom right
        for i in range(1,10):
            for r in range(6,9):
                for c in range(6,9):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)

    def isComplete(self):
        for i in range(9):
            for n in range(9):
                if self.puzzleGrid.grid[i][n].isSolved:
                    continue
                else:
                    return False
        return True

    def RemovePossiblityFromTargetCell(self,i,targetCell):
        if i in targetCell.possibilities:
            targetCell.possibilities.remove(i)

    def flatten_list(self, list_of_lists): #flattens a list of lists into single array
        flat_list = []
        for sublist in list_of_lists:
            if type(sublist) is list: #make sure the item in list_of_lists is a list (iterable)
                for item in sublist:
                    flat_list.append(item)
        flat_list = list(dict.fromkeys(flat_list))
        return flat_list


root = Tk()
app = App(root)
cell = app.puzzleGrid.grid[4][4]

root.mainloop()
#root.destroy()
