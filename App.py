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
        master.geometry('550x600+0+0')
        top_title_header = Frame(self.master,width = 600, height = 50)
        top_title_header.pack()

        #botTitleHeader = Frame(self.master,width = 600, height = 10)
        #botTitleHeader.pack()

        top_frame = Frame(self.master,width = 600, height = 600)
        top_frame.pack()

        #create input elements and assign to SDKgrid
        for x in range(9):
            for y in range(9):
                input = Entry(top_frame, width = 2, font = ("Courier", 24), justify="center")
                self.puzzleGrid.get_cell_at_coords(x,y).entryBox = input
                input.grid(row=x,column=y)

        #separate grid and buttons
        grid_to_label_spacer = Frame(width = 600, height = 10)
        grid_to_label_spacer.pack()

        #label for messages
        self.message = StringVar()
        self.message.set("LOAD or manually input a puzzle!")
        self.label_for_messages = Label(self.master, textvariable = self.message)
        self.label_for_messages.pack()

        #separate grid and buttons
        label_to_button_spacer = Frame(width = 600, height = 10)
        label_to_button_spacer.pack()

        #container for buttons
        bottom_frame = Frame( width = 600, height = 50)
        bottom_frame.pack()

        solve_button = Button(bottom_frame, text = "SOLVE", fg = "blue", command=lambda : self.solve_button())
        solve_button.pack(side=LEFT)

        step_button = Button(bottom_frame, text = "STEP", fg = "black", command=lambda : self.step_button())
        step_button.pack(side=LEFT)

        populate_button = Button(bottom_frame, text = "LOAD", fg = "black", command=lambda : self.load())
        populate_button.pack(side=LEFT)

        save_button = Button(bottom_frame, text = "SAVE", fg = "black", command=lambda : self.save())
        save_button.pack(side=LEFT)

        quit_button = Button(bottom_frame, text = "QUIT", fg = "red", command=bottom_frame.quit)
        quit_button.pack(side=LEFT)

    def step_button(self):
        self.foundStep = False
        if self.puzzleGrid.assign_input_values():
            for i in range(30): #[BUG]  iteration based?
                for x in range(9):
                    for y in range(9):
                        if self.foundStep == False:
                            self.solve_step(x,y)

        if self.isComplete() == True:
            self.message.set("Puzzle completed!")

    def load(self,file = ""):
        self.puzzleGrid.clear()
        if file == "":
            file = filedialog.askopenfilename(initialdir="puzzles/",title="Select file", filetypes =(("JSON files","*.json"),("All file types","*.*")))
        if file != "": #check again incase dialog is cancelled
            self.puzzleGrid.load(file)
            self.message.set("SOLVE the puzzle or STEP through the solution!")

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
            pdb.set_trace()
            if isinstance(fout, str):
                self.puzzleGrid.save(fout)
        else:
            self.message.set("Bad Input! Make sure you've entered only single digits!")

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
                self.calculate_possibilities()
                if len(self.targetCell.possibilities) == 1:
                    self.targetCell.solve()
                    self.foundStep = True
                else:
                    self.check_neighbours()

    def calculate_possibilities(self):
        self.reduce_possibilities_by_row()
        self.reduce_possibilities_by_column()
        self.reduce_possibilities_by_box()

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

    def reduce_possibilities_by_row(self):
        #check for numbers in horizontal adjacent cells and remove those from target's possibilities
        x = self.targetCell.x
        for i in range(1,10): #content
            for n in range(9): #y-coord adjacent cells
                if self.targetCell != self.puzzleGrid.grid[x][n]:
                    self.targetCell.row_neighbour_possibilities.append( self.puzzleGrid.grid[x][n].possibilities)
                if str(i) == self.puzzleGrid.grid[x][n].finalNumber:
                    self.RemovePossiblityFromTargetCell(i,self.targetCell)
        self.targetCell.row_neighbour_possibilities = self.flatten_list(self.targetCell.row_neighbour_possibilities)

    def reduce_possibilities_by_column(self):
        #check for numbers in vertical adjacent cells and remove those from target's possibilities
        y = self.targetCell.y
        for i in range(1,10): #content
            for n in range(9): #x-coord adjacent cells
                if self.targetCell != self.puzzleGrid.grid[n][y]:
                    self.targetCell.column_neighbour_possibilities.append( self.puzzleGrid.grid[n][y].possibilities)
                if str(i) == self.puzzleGrid.grid[n][y].finalNumber:
                    self.RemovePossiblityFromTargetCell(i,self.targetCell)
        self.targetCell.column_neighbour_possibilities = self.flatten_list(self.targetCell.column_neighbour_possibilities)

    def reduce_possibilities_by_box(self):
        #check 3x3 box that contains targetCell for numbers and remove them from target possibilities
        x = self.targetCell.x
        y = self.targetCell.y
        if x < 3 and y < 3: #top left
            self.check_box1()
        if x > 2 and x < 6 and y < 3: #middle left
            self.check_box2()
        if x > 5 and y < 3: #bottom left
            self.check_box3()
        if x < 3 and y > 2 and y < 6: #top middle
            self.check_box4()
        if x > 2 and x < 6 and y > 2 and y < 6: #center
            self.check_box5()
        if x > 5 and y > 2 and y < 6: #bottom middle
            self.check_box6()
        if x < 3 and y > 5: #top right
            self.check_box7()
        if x > 2 and x < 6 and y > 5: #middle right
            self.check_box8()
        if x > 5 and y > 5: #bottom right
            self.check_box9()
        self.targetCell.box_neighbour_possibilities = self.flatten_list(self.targetCell.box_neighbour_possibilities)

    def check_box1(self):  #top left
        for i in range(1,10): #[BUG] could move this below to save time?
            for r in range(0,3):
                for c in range(0,3):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)
    def check_box2(self): #middle left
        for i in range(1,10):
            for r in range(3,6):
                for c in range(0,3):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)
    def check_box3(self): #bottom left
        for i in range(1,10):
            for r in range(6,9):
                for c in range(0,3):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)
    def check_box4(self): #top middle
        for i in range(1,10):
            for r in range(0,3):
                for c in range(3,6):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)
    def check_box5(self): #center
        for i in range(1,10):
            for r in range(3,6):
                for c in range(3,6):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)
    def check_box6(self): #bottom middle
        for i in range(1,10):
            for r in range(6,9):
                for c in range(3,6):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)
    def check_box7(self): #top right
        for i in range(1,10):
            for r in range(0,3):
                for c in range(6,9):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)
    def check_box8(self): #middle right
        for i in range(1,10):
            for r in range(3,6):
                for c in range(6,9):
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( self.puzzleGrid.grid[r][c].possibilities)
                    if str(i) == self.puzzleGrid.grid[r][c].finalNumber:
                        self.RemovePossiblityFromTargetCell(i,self.targetCell)
    def check_box9(self): #bottom right
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
root.title("SuDuKo Solver")

app = App(root)
cell = app.puzzleGrid.grid[4][4]

root.mainloop()
#root.destroy()
