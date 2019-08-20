from SDKCell import *
import json

class SDKGrid:
    def __init__(self, cellContent):
        self.grid = []
        for i in range(9):
            self.grid.append(self.make_row(cellContent))
        self.assign_cell_coords()

    def make_row(self, cellContent):
        row = []
        for i in range(9):
            cell = SDKCell(cellContent)
            row.append(cell)
        return row

    def assign_cell_coords(self):
        for x in range(9):
            for y in range(9):
                self.grid[x][y].x = x
                self.grid[x][y].y = y

    def get_cell_at_coords(self, x, y):
        return self.grid[x][y]

    def clear(self):
        for x in range(9):
            for y in range(9):
                self.grid[x][y].clear()

    def assign_input_values(self):
        for x in range(9):
            for y in range(9):
                if self.grid[x][y].assign_value_from_input_box():
                    continue
                else:
                    return False
        return True

    def load(self, filePath):
        with open(filePath, "r") as read_file:
            data = json.load(read_file)
        for item in data:
            x = item["x"]
            y = item["y"]
            value = item["value"]
            self.grid[x][y].load(value)

    def save(self,filePath):
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
