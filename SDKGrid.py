import json
from SDKCell import *

class SDKGrid:
    """This object represents the entire SuDoKu puzzle grid and is comprised of SDKCells"""

    def __init__(self, cellContent):
        """create a 9x9 2D array of SDK cells"""
        self.grid = []
        for x in range(9):
            self.grid.append(self.make_row(x, cellContent))
        
    def make_row(self, rowIndex, cellContent):
        """create a row of cells containing cellContent"""
        row = []
        for columnIndex in range(9):
            cell = SDKCell(cellContent)
            cell.x = rowIndex
            cell.y = columnIndex
            row.append(cell)
        return row

    def get_cell_at_coords(self, x, y):
        return self.grid[x][y]

    def clear_grid(self):
        for x in range(9):
            for y in range(9):
                self.grid[x][y].clear()

    def assign_input_values(self):
        """assign the values present in the Entry widgets to the SKDCell's finalNumber"""
        for x in range(9):
            for y in range(9):
                if self.grid[x][y].assign_value_from_input_box():
                    continue
                else:
                    return False
        return True

    def load(self, filePath):
        """load SDKGrid data from a .json file"""
        with open(filePath, "r") as read_file:
            data = json.load(read_file)
        for item in data:
            x = item["x"]
            y = item["y"]
            value = item["value"]
            self.grid[x][y].load(value)

    def save(self,filePath):
        """save SDKGrid data to a .json file"""
        data = []
        for x in range(9):
            for y in range(9):
                cell = {}
                cell["x"] = x
                cell["y"] = y
                cell["value"] = self.grid[x][y].finalNumber
                data.append(cell)
        with open(filePath, "w") as outfile:
            json.dump(data,outfile)
