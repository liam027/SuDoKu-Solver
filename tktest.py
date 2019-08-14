from tkinter import *
from SDKGrid import *
from SDKCell import *
from Solver import *

class App:
    def __init__(self, master, **kwargs):
        #generate new SDKgrid for future input value storage
        self.puzzleGrid = SDKGrid("")

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

        solveButton = Button(bottomFrame, text = "SOLVE", fg = "blue", command=lambda : self.solve())
        solveButton.pack(side=LEFT)

        showButton = Button(bottomFrame, text = "SHOW", fg = "black", command=lambda : self.show_target())
        showButton.pack(side=LEFT)

        populateButton = Button(bottomFrame, text = "POPULATE", fg = "black", command=lambda : self.populate())
        populateButton.pack(side=LEFT)

        quitButton = Button(bottomFrame, text = "QUIT", fg = "red", command=bottomFrame.quit)
        quitButton.pack(side=LEFT)

    def say_hi(self):
        print("hi there, everyone!")

    def populate(self):
        self.puzzleGrid.populate("trial.json")

    def solve(self):
        if self.puzzleGrid.assign_input_values():
            print("Inputs valid!")
            #[BUG] iteration based?
            for i in range(30):
                self.reduce_possibilities()

            if self.isComplete() == True:
                print("Puzzle Completed!")
                self.puzzleGrid.display_solution_values()
            else:
                print("Puzzle NOT Complete!")
                self.puzzleGrid.display_solution_values()
        else:
            print("Inputs not valid!")



    def reduce_possibilities(self):
        for x in range(9):
            for y in range(9):
                if self.puzzleGrid.grid[x][y].isSolved == False:
                    self.check_row(x,y)
                    self.check_column(x,y)
                    self.check_box(x,y)
                    if len(self.puzzleGrid.grid[x][y].possibilities) == 1:
                        self.puzzleGrid.grid[x][y].solve()

    def check_row(self,x,y):
        for i in range(1,10): #content
            for n in range(9): #y-coord adjacent cells
                if str(i) == self.puzzleGrid.grid[x][n].finalNumber:
                    if i in self.puzzleGrid.grid[x][y].possibilities:
                        self.puzzleGrid.grid[x][y].possibilities.remove(i)

    def check_column(self,x,y):
        for i in range(1,10): #content
            for n in range(9): #x-coord adjacent cells
                  if str(i) == self.puzzleGrid.grid[n][y].finalNumber:
                    if i in self.puzzleGrid.grid[x][y].possibilities:
                        self.puzzleGrid.grid[x][y].possibilities.remove(i)

    def check_box(self, x,y):
        #box 1
        if x < 3 and y < 3:
            for i in range(1,10):
                for r in range(0,3):
                    for c in range(0,3):
                        if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                            if i in self.puzzleGrid.grid[x][y].possibilities:
                                self.puzzleGrid.grid[x][y].possibilities.remove(i)
        # box 2
        if x > 2 and x < 6 and y < 3:
            for i in range(1,10):
                for r in range(3,6):
                    for c in range(0,3):
                        if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                            if i in self.puzzleGrid.grid[x][y].possibilities:
                                self.puzzleGrid.grid[x][y].possibilities.remove(i)
        # box 3
        if x > 5 and y < 3:
            for i in range(1,10):
                for r in range(6,9):
                    for c in range(0,3):
                        if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                            if i in self.puzzleGrid.grid[x][y].possibilities:
                                self.puzzleGrid.grid[x][y].possibilities.remove(i)
        # box 4
        if x < 3 and y > 2 and y < 6:
            for i in range(1,10):
                for r in range(0,3):
                    for c in range(3,6):
                        if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                            if i in self.puzzleGrid.grid[x][y].possibilities:
                                self.puzzleGrid.grid[x][y].possibilities.remove(i)
        # box 5
        if x > 2 and x < 6 and y > 2 and y < 6:
            for i in range(1,10):
                for r in range(3,6):
                    for c in range(3,6):
                        if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                            if i in self.puzzleGrid.grid[x][y].possibilities:
                                self.puzzleGrid.grid[x][y].possibilities.remove(i)
        # box 6
        if x > 5 and y > 2 and y < 6:
            for i in range(1,10):
                for r in range(6,9):
                    for c in range(3,6):
                        if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                            if i in self.puzzleGrid.grid[x][y].possibilities:
                                self.puzzleGrid.grid[x][y].possibilities.remove(i)
        # box 7
        if x < 3 and y > 5:
            for i in range(1,10):
                for r in range(0,3):
                    for c in range(6,9):
                        if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                            if i in self.puzzleGrid.grid[x][y].possibilities:
                                self.puzzleGrid.grid[x][y].possibilities.remove(i)
        # box 8
        if x > 2 and x < 6 and y > 5:
            for i in range(1,10):
                for r in range(3,6):
                    for c in range(6,9):
                        if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                            if i in self.puzzleGrid.grid[x][y].possibilities:
                                self.puzzleGrid.grid[x][y].possibilities.remove(i)
        # box 9
        if x > 5 and y > 5:
            for i in range(1,10):
                for r in range(6,9):
                    for c in range(6,9):
                        if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                            if i in self.puzzleGrid.grid[x][y].possibilities:
                                self.puzzleGrid.grid[x][y].possibilities.remove(i)

    def isComplete(self):
        for i in range(9):
            for n in range(9):
                if self.puzzleGrid.grid[i][n].isSolved:
                    continue
                else:
                    return False
        return True

root = Tk()

app = App(root)

root.mainloop()
#root.destroy()
