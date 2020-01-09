**SUDOKU SOLVER**

A small app that solves SuDoKu puzzles using a logical approach, as a person would. It does **not** use brute force or iterative guessing.

**Running the app**

Clone this repo and run App.py using Python3:

    $ git clone git@github.com:liam027/SuDoKu-Solver.git
    $ python3 App.py

**Features**
  - UI for user input of a puzzle (tkinter)
  - Save or load a puzzle to/from a .json file
  - Solve a puzzle in full or one cell at a time (step-wise)
  - A test case which allows for unit testing of the different solving techniques

**Methodology**

Generates a SuDoKu grid (SDKGrid) comprised of individual cell (SDKCells) that contain the puzzle information. When solving, the app considers the following approaches:

*Method #1:* 

Reduce and assess individual cell possibilities "calculate_possibilities()"
Each cell is aware of all values it could possibly be (cell.possiblities, 1 through 9 to start). If a possible value is present
in another cell in its row, column or box, that possibility is removed. Once a cell has only once possibility, it can be solved.

*Method #2:* 

Assess row, column and box possibilities "check_neighbours()"
Each cell is also aware of the possiblities of its neighbouring cells. If a cell is the only one that contains a certain possibility, it can be solved.
Ie. in row if only one cell has the possibility to be a 1, it can be solved.

*Method #3:*

Reduce possiblities by neighbouring possibility pairs (Y-wing method)
TO BE IMPLEMENTED
