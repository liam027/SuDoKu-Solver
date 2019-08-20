import App
from tkinter import *
import unittest

class SolverTests(unittest.TestCase):
    print("Tests initiated!")

    def test_load(self):
        root = Tk()
        app = App.App(root)
        app.load("puzzles/test.json")
        app.puzzleGrid.assign_input_values()
        self.assertEqual(app.puzzleGrid.grid[0][0].finalNumber, "9" )
        self.assertEqual(app.puzzleGrid.grid[2][4].finalNumber, "2" )
        self.assertEqual(app.puzzleGrid.grid[7][8].finalNumber, "4" )


    def test_reduce_possiblities(self):
        root = Tk()
        app = App.App(root)
        app.load("puzzles/test.json")
        app.puzzleGrid.assign_input_values()
        app.solve_step(0,8)
        app.foundStep = False
        self.assertEqual(app.puzzleGrid.grid[0][8].finalNumber, "1")
        app.foundStep = False
        app.solve_step(8,0)
        self.assertEqual(app.puzzleGrid.grid[8][0].finalNumber, "1")
        app.foundStep = False
        app.solve_step(2,2)
        self.assertEqual(app.puzzleGrid.grid[2][2].finalNumber, "1")

    def test_check_neighbours_by_row(self):
        root = Tk()
        app = App.App(root)
        app.load("puzzles/test.json")
        app.puzzleGrid.assign_input_values()
        app.solve_step(7,2)
        app.foundStep = False
        app.solve_step(7,4)
        app.foundStep = False
        app.solve_step(7,6)
        app.check_neighbours()
        self.assertEqual(app.puzzleGrid.grid[7][6].finalNumber, "5")

    def test_check_neighbours_by_column(self):
        root = Tk()
        app = App.App(root)
        app.load("puzzles/test.json")
        app.puzzleGrid.assign_input_values()
        app.solve_step(4,4)
        app.foundStep = False
        app.solve_step(5,4)
        app.foundStep = False
        app.solve_step(7,4)
        app.foundStep = False
        app.solve_step(8,4)
        app.check_neighbours()
        self.assertEqual(app.puzzleGrid.grid[8][4].finalNumber, "4")

    def test_check_neighbours_by_box(self):
        root = Tk()
        app = App.App(root)
        app.load("puzzles/test.json")
        app.puzzleGrid.assign_input_values()
        app.solve_step(3,6)
        app.foundStep = False
        app.solve_step(3,7)
        app.foundStep = False
        app.solve_step(4,7)
        app.foundStep = False
        app.solve_step(4,8)
        app.foundStep = False
        app.solve_step(5,6)
        app.foundStep = False
        app.solve_step(5,7)
        app.foundStep = False
        app.solve_step(5,8)
        app.foundStep = False
        app.solve_step(3,8)
        app.check_neighbours()
        self.assertEqual(app.puzzleGrid.grid[3][8].finalNumber, "8")

if __name__ == '__main__':
    unittest.main(verbosity=2)
