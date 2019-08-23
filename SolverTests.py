import App
from tkinter import *
import unittest

class SolverTests(unittest.TestCase):
    """A few (non-exhaustive) test cases for a hypothetical test puzzle to ensure solving methodology is behaving as expected"""
    print("SolverTests initiated!")
    def test_load(self):
        """Load test file and check if values are assigned correctly to SDKGrid"""
        root = Tk()
        app = App.App(root)
        app.load("puzzles/test.json")
        app.puzzleGrid.assign_input_values()
        self.assertEqual(app.puzzleGrid.grid[0][0].finalNumber, "9" )
        self.assertEqual(app.puzzleGrid.grid[2][4].finalNumber, "2" )
        self.assertEqual(app.puzzleGrid.grid[7][8].finalNumber, "4" )


    def test_reduce_possiblities(self):
        """For 3 cases (row, column, box), assert that a cell will solve when it's possibilities are reduced to zero"""
        root = Tk()
        app = App.App(root)
        app.load("puzzles/test.json")
        app.puzzleGrid.assign_input_values()
        app.solver.solve_step(app.puzzleGrid,0,8)
        app.foundStep = False
        self.assertEqual(app.puzzleGrid.grid[0][8].finalNumber, "1")
        app.foundStep = False
        app.solver.solve_step(app.puzzleGrid,8,0)
        self.assertEqual(app.puzzleGrid.grid[8][0].finalNumber, "1")
        app.foundStep = False
        app.solver.solve_step(app.puzzleGrid,2,2)
        self.assertEqual(app.puzzleGrid.grid[2][2].finalNumber, "1")

    def test_check_neighbours_by_row(self):
        """Assert that a cell will solve when it is the only cell in a row that can contain that number"""
        root = Tk()
        app = App.App(root)
        app.load("puzzles/test.json")
        app.puzzleGrid.assign_input_values()
        app.solver.solve_step(app.puzzleGrid,7,2)
        app.foundStep = False
        app.solver.solve_step(app.puzzleGrid,7,4)
        app.foundStep = False
        app.solver.solve_step(app.puzzleGrid,7,6)
        app.solver.check_neighbours()
        self.assertEqual(app.puzzleGrid.grid[7][6].finalNumber, "5")

    def test_check_neighbours_by_column(self):
        """Assert that a cell will solve when it is the only cell in a column that can contain that number"""
        root = Tk()
        app = App.App(root)
        app.load("puzzles/test.json")
        app.puzzleGrid.assign_input_values()
        app.solver.solve_step(app.puzzleGrid,4,4)
        app.foundStep = False
        app.solver.solve_step(app.puzzleGrid,5,4)
        app.foundStep = False
        app.solver.solve_step(app.puzzleGrid,7,4)
        app.foundStep = False
        app.solver.solve_step(app.puzzleGrid,8,4)
        app.solver.check_neighbours()
        self.assertEqual(app.puzzleGrid.grid[8][4].finalNumber, "4")

    def test_check_neighbours_by_box(self):
        """Assert that a cell will solve when it is the only cell in a box that can contain that number"""
        root = Tk()
        app = App.App(root)
        app.load("puzzles/test.json")
        app.puzzleGrid.assign_input_values()
        app.solver.solve_step(app.puzzleGrid,3,6)
        app.foundStep = False
        app.solver.solve_step(app.puzzleGrid,3,7)
        app.foundStep = False
        app.solver.solve_step(app.puzzleGrid,4,7)
        app.foundStep = False
        app.solver.solve_step(app.puzzleGrid,4,8)
        app.foundStep = False
        app.solver.solve_step(app.puzzleGrid,5,6)
        app.foundStep = False
        app.solver.solve_step(app.puzzleGrid,5,7)
        app.foundStep = False
        app.solver.solve_step(app.puzzleGrid,5,8)
        app.foundStep = False
        app.solver.solve_step(app.puzzleGrid,3,8)
        app.solver.check_neighbours()
        self.assertEqual(app.puzzleGrid.grid[3][8].finalNumber, "8")

if __name__ == '__main__':
    unittest.main(verbosity=2)
