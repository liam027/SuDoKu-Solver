from FlattenList import *

class Solver:
    puzzleGrid = None

    def __init__(self):
        self.targetCell = None
        self.foundStep = False

    def solve_step(self,puzzle_grid,x,y):
        self.puzzleGrid  = puzzle_grid
        if(self.foundStep == False):
            self.targetCell = self.puzzleGrid.grid[x][y]
            if(self.targetCell.isSolved == False):
                self.calculate_possibilities()
                if len(self.targetCell.possibilities) == 1:
                    self.targetCell.solve()
                    return True
                else:
                    return self.check_neighbours()

    def solve_full(self,puzzle_grid,x,y):
        self.puzzleGrid = puzzle_grid
        self.targetCell = self.puzzleGrid.grid[x][y]
        if(self.targetCell.isSolved == False):
            self.calculate_possibilities()
            if len(self.targetCell.possibilities) == 1:
                self.targetCell.solve()
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
                    return True
                elif p not in self.targetCell.column_neighbour_possibilities:
                    self.targetCell.solve(p)
                    return True
                elif p not in self.targetCell.box_neighbour_possibilities:
                    self.targetCell.solve(p)
                    return True
                else:
                    return False

    def reduce_possibilities_by_row(self):
        #check for numbers in horizontal adjacent cells and remove those from target's possibilities
        x = self.targetCell.x
        for i in range(1,10): #content
            for n in range(9): #y-coord adjacent cells
                neighbour_cell = self.puzzleGrid.grid[x][n]
                if self.targetCell != neighbour_cell:
                    self.targetCell.row_neighbour_possibilities.append( neighbour_cell.possibilities)
                if str(i) == neighbour_cell.finalNumber:
                    self.RemovePossiblityFromTargetCell(i)
        self.targetCell.row_neighbour_possibilities = flatten_list(self.targetCell.row_neighbour_possibilities)

    def reduce_possibilities_by_column(self):
        #check for numbers in vertical adjacent cells and remove those from target's possibilities
        y = self.targetCell.y
        for i in range(1,10): #content
            for n in range(9): #x-coord adjacent cells
                neighbour_cell = self.puzzleGrid.grid[n][y]
                if self.targetCell != neighbour_cell:
                    self.targetCell.column_neighbour_possibilities.append( neighbour_cell.possibilities)
                if str(i) == neighbour_cell.finalNumber:
                    self.RemovePossiblityFromTargetCell(i)
        self.targetCell.column_neighbour_possibilities = flatten_list(self.targetCell.column_neighbour_possibilities)

    def reduce_possibilities_by_box(self):
        #check 3x3 box that contains self.targetCell for numbers and remove them from target possibilities
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
        self.targetCell.box_neighbour_possibilities = flatten_list(self.targetCell.box_neighbour_possibilities)

    def check_box1(self):  #top left
        for i in range(1,10): #[BUG] could move this below to save time?
            for r in range(0,3):
                for c in range(0,3):
                    neighbour_cell = self.puzzleGrid.grid[r][c]
                    if self.targetCell != neighbour_cell:
                        self.targetCell.box_neighbour_possibilities.append( neighbour_cell.possibilities)
                    if str(i) == neighbour_cell.finalNumber:
                        self.RemovePossiblityFromTargetCell(i)
    def check_box2(self): #middle left
        for i in range(1,10):
            for r in range(3,6):
                for c in range(0,3):
                    neighbour_cell = self.puzzleGrid.grid[r][c]
                    if self.targetCell != neighbour_cell:
                        self.targetCell.box_neighbour_possibilities.append( neighbour_cell.possibilities)
                    if str(i) == neighbour_cell.finalNumber:
                        self.RemovePossiblityFromTargetCell(i)
    def check_box3(self): #bottom left
        for i in range(1,10):
            for r in range(6,9):
                for c in range(0,3):
                    neighbour_cell = self.puzzleGrid.grid[r][c]
                    if self.targetCell != neighbour_cell:
                        self.targetCell.box_neighbour_possibilities.append( neighbour_cell.possibilities)
                    if str(i) == neighbour_cell.finalNumber:
                        self.RemovePossiblityFromTargetCell(i)
    def check_box4(self): #top middle
        for i in range(1,10):
            for r in range(0,3):
                for c in range(3,6):
                    neighbour_cell = self.puzzleGrid.grid[r][c]
                    if self.targetCell != neighbour_cell:
                        self.targetCell.box_neighbour_possibilities.append( neighbour_cell.possibilities)
                    if str(i) == neighbour_cell.finalNumber:
                        self.RemovePossiblityFromTargetCell(i)
    def check_box5(self): #center
        for i in range(1,10):
            for r in range(3,6):
                for c in range(3,6):
                    neighbour_cell = self.puzzleGrid.grid[r][c]
                    if self.targetCell != self.puzzleGrid.grid[r][c]:
                        self.targetCell.box_neighbour_possibilities.append( neighbour_cell.possibilities)
                    if str(i) == neighbour_cell.finalNumber:
                        self.RemovePossiblityFromTargetCell(i)
    def check_box6(self): #bottom middle
        for i in range(1,10):
            for r in range(6,9):
                for c in range(3,6):
                    neighbour_cell = self.puzzleGrid.grid[r][c]
                    if self.targetCell != neighbour_cell:
                        self.targetCell.box_neighbour_possibilities.append( neighbour_cell.possibilities)
                    if str(i) == neighbour_cell.finalNumber:
                        self.RemovePossiblityFromTargetCell(i)
    def check_box7(self): #top right
        for i in range(1,10):
            for r in range(0,3):
                for c in range(6,9):
                    neighbour_cell = self.puzzleGrid.grid[r][c]
                    if self.targetCell != neighbour_cell:
                        self.targetCell.box_neighbour_possibilities.append( neighbour_cell.possibilities)
                    if str(i) == neighbour_cell.finalNumber:
                        self.RemovePossiblityFromTargetCell(i)
    def check_box8(self): #middle right
        for i in range(1,10):
            for r in range(3,6):
                for c in range(6,9):
                    neighbour_cell = self.puzzleGrid.grid[r][c]
                    if self.targetCell != neighbour_cell:
                        self.targetCell.box_neighbour_possibilities.append( neighbour_cell.possibilities)
                    if str(i) == neighbour_cell.finalNumber:
                        self.RemovePossiblityFromTargetCell(i)
    def check_box9(self): #bottom right
        for i in range(1,10):
            for r in range(6,9):
                for c in range(6,9):
                    neighbour_cell = self.puzzleGrid.grid[r][c]
                    if self.targetCell != neighbour_cell:
                        self.targetCell.box_neighbour_possibilities.append( neighbour_cell.possibilities)
                    if str(i) == neighbour_cell.finalNumber:
                        self.RemovePossiblityFromTargetCell(i)

    def RemovePossiblityFromTargetCell(self,i):
        if i in self.targetCell.possibilities:
            self.targetCell.possibilities.remove(i)
