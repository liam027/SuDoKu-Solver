
class Solver:
    def __init__(self, _puzGrid, _possGrid):
        self.puzGrid = _puzGrid
        self.possGrid = _possGrid
        #[BUG] iteration based?
        for i in range(10):
            self.update_all_cells()
            if self.is_complete_checker() == True:
                print("Puzzle Completed!")
                return _puzGrid

    def update_all_cells(self):
        for i in range(9):
            for n in range(9):
                if self.puzGrid[i][n] == "":
                    self.check_row(i,n)
                    self.check_column(i,n)
                    #check_box(i,n)
                    if len(self.possGrid[i][n]) == 1:
                        self.puzGrid[i][n] = self.possGrid[i][n][0]
                else:
                    self.possGrid[i][n] = ""

    def check_row(self,x,y):
        for i in range(1,10):
            for n in range(9):
                if i == self.puzGrid[x][n]:
                    if i in self.possGrid[x][y]:
                        self.possGrid[x][y].remove(i)

    def check_column(self,x,y):
        for i in range(1,10):
            for n in range(9):
                  if i == self.puzGrid[n][y]:
                    if i in self.possGrid[x][y]:
                        self.possGrid[x][y].remove(i)

    def is_complete_checker(self):
        for i in range(9):
            for n in range(9):
                if self.possGrid[i][n] != "":
                    return False
        return True
