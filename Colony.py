from cell import *
class Colony:

    def __init__(self, rows, columns):
        #remember to number rows and columns
        self.rows = rows
        self.columns = columns

        #create a cell as a reference to a list of references to rows
        self.cells=[]

        for row in range(rows):
            self.cells.append([])    #start with an empty row

            for columns in range(columns):
                self.cells[row].append(Cell(row, columns))






