from logic.SDKCell import *
from logic.SDKGrid import *
import logic.Solver as Solver
from tkinter import filedialog
from tkinter import *

class App:
    def __init__(self, master, **kwargs):
        self.puzzleGrid = SDKGrid("")
        self.solver = Solver.Solver()

        self.master=master
        master.geometry('450x500+0+0')

        top_title_header = Frame(self.master,width = 450, height = 25)
        top_title_header.pack()
        top_frame = Frame(self.master,width = 450, height = 500)
        top_frame.pack()
        #create input (entry) widgets and assign to SDKgrid
        for x in range(9):
            for y in range(9):
                input = Entry(top_frame, width = 2, font = ("Courier", 24), justify="center")
                self.puzzleGrid.get_cell_at_coords(x,y).entryBox = input
                input.grid(row=x,column=y)

        grid_to_label_spacer = Frame(width = 450, height = 10)
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

        """Button Widgets"""
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

    """Button methods"""
    def solve_button(self):
        """solves the entire puzzle"""
        if self.puzzleGrid.assign_input_values():
            for i in range(30): #[NOTE] num of iterations can be tweaked
                for x in range(9):
                    for y in range(9):
                        self.solver.solve_full(self.puzzleGrid,x,y)
        else:
            print("Bad Input! Make sure you've entered only single digits!")
        if self.isComplete() == True:
            self.message.set("Puzzle completed!")
        else:
            self.message.set("Puzzle completed!")

    def step_button(self):
        """solves one cell of the the puzzle"""
        self.foundStep = False
        if self.puzzleGrid.assign_input_values():
            for x in range(9):
                for y in range(9):
                    if self.foundStep == False:
                        if(self.solver.solve_step(self.puzzleGrid,x,y)):
                            self.foundStep = True
        if self.isComplete() == True:
            self.message.set("Puzzle completed!")

    def save(self):
        """saves the current input as a .json puzzle"""
        if self.puzzleGrid.assign_input_values():
            fout = filedialog.asksaveasfilename(initialdir="puzzles/",title="Select save location", filetypes =(("JSON files","*.json"),("All file types","*.*")))
            if fout != "" and isinstance(fout, str):
                self.puzzleGrid.save(fout)
        else:
            self.message.set("Bad Input! Make sure you've entered only single digits!")

    def load(self,file = ""):
        """load a .json puzzle"""
        if file == "":
            file = filedialog.askopenfilename(initialdir="puzzles/",title="Select file", filetypes =(("JSON files","*.json"),("All file types","*.*")))
        if file != "" and isinstance(file, str): #check again incase dialog is cancelled
            self.puzzleGrid.clear_grid()
            self.puzzleGrid.load(file)
            self.message.set("SOLVE the puzzle or STEP through the solution!")

    def print_remaining_cells_possibilities(self):
        for x in range(9):
            for y in range(9):
                cell = self.puzzleGrid.grid[x][y]
                if cell.isSolved == False:
                    print(f'@{x},{y}: {cell.possibilities}')

    def isComplete(self):
        """check if puzzle is complete"""
        for i in range(9):
            for n in range(9):
                if self.puzzleGrid.grid[i][n].isSolved:
                    continue
                else:
                    return False
        return True

root = Tk()
root.title("SuDoKu Solver")
app = App(root)
root.mainloop()
#root.destroy()
