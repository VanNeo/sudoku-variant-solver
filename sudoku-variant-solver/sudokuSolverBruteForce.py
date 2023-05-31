import time
import copy
import tkinter as tk
from abc import (
  ABC,
  abstractmethod,
)
# root = tk.Tk()

# root.geometry("500x500")
# root.title("Sudoku Interface")

# root.mainloop()

startTime = time.time()

template = [[-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1]]

puzzle = [[4, 5, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, 2, -1, 7, -1, 6, 3, -1],
        [-1, -1, -1, -1, -1, -1, -1, 2, 8],
        [-1, -1, -1, 9, 5, -1, -1, -1, -1],
        [-1, 8, 6, -1, -1, -1, 2, -1, -1],
        [-1, 2, -1, 6, -1, -1, 7, 5, -1],
        [-1, -1, -1, -1, -1, -1, 4, 7, 6],
        [-1, 7, -1, -1, 4, 5, -1, -1, -1],
        [-1, -1, 8, -1, -1, 9, -1, -1, -1]]

# puzzle = [[[4, 5, -1, -1, -1, -1, -1, -1, -1],
#         [-1, -1, 2, -1, 7, -1, 6, 3, -1],
#         [-1, -1, -1, -1, -1, -1, -1, 2, 8],
#         [-1, -1, -1, 9, 5, -1, -1, -1, -1],
#         [-1, 8, 6, -1, -1, -1, 2, -1, -1],
#         [-1, 2, -1, 6, -1, -1, 7, 5, -1],
#         [-1, -1, -1, -1, -1, -1, 4, 7, 6],
#         [-1, 7, -1, -1, 4, 5, -1, -1, -1],
#         [-1, -1, 8, -1, -1, 9, -1, -1, -1]],
#         [[-1, -1, -1, -1, -1, -1, -1, -1, -1],
#         [-1, -1, -1, -1, -1, -1, -1, -1, -1],
#         [-1, -1, -1, -1, -1, -1, -1, -1, -1],
#         [-1, -1, -1, -1, -1, -1, -1, -1, -1],
#         [-1, -1, -1, -1, -1, -1, -1, -1, -1],
#         [-1, -1, -1, -1, -1, -1, -1, -1, -1],
#         [-1, -1, -1, -1, -1, -1, -1, -1, -1],
#         [-1, -1, -1, -1, -1, -1, -1, -1, -1],
#         [-1, -1, -1, -1, -1, -1, -1, -1, -1]]]

# puzzle = [[4, 5, 3, 8, 2, 6, 1, 9, 7],
#         [8, 9, 2, 5, 7, 1, 6, 3, 4],
#         [1, 6, 7, 4, 9, 3, 5, 2, 8],
#         [7, 1, 4, 9, 5, 2, 8, 6, 3],
#         [5, 8, 6, 1, 3, 7, 2, 4, 9],
#         [3, 2, 9, 6, 8, 4, 7, 5, 1],
#         [9, 3, 5, 2, 1, 8, 4, 7, 6],
#         [6, 7, 1, 3, 4, 5, 9, 8, 2],
#         [2, 4, 8, 7, 6, 9, 3, 1, 5]]

class sudoku():

    def __init__(self):
        self.sudokuRows = []
        self.sudokuColumns = []
        self.sudokuBoxes = []
        self.sudokuMatrix = []
        self.createConstraints()

    def createConstraints(self):
        for i in range(9):
            newRow = sudokuRow(i)
            newColumn = sudokuColumn(i)
            newBox = sudokuBox(i)

            self.sudokuRows.append(newRow)
            self.sudokuColumns.append(newColumn)
            self.sudokuBoxes.append(newBox)

    def makeMatrix(self):
        pass

    def findRow(self, index):
        for sudokuRow in self.sudokuRows:
            if sudokuRow.index == index:
                return sudokuRow
            
    def findColumn(self, index):
        for sudokuColumn in self.sudokuColumns:
            if sudokuColumn.index == index:
                return sudokuColumn
            
    def findBox(self, index):
        for sudokuBox in self.sudokuBoxes:
            if sudokuBox.index == index:
                return sudokuBox
            
    def printSudoku(self):
        print(" ----------------------")

        for row in self.sudokuMatrix:
            for col in row:
                if col.sudokuColumn.index == 0 or col.sudokuColumn.index == 3 or col.sudokuColumn.index == 6: 
                    print("", end="| ")
                if col.value == -1:
                    print("x", end=" ")
                else:
                    print(col.value, end=" ")
                if col.sudokuColumn.index == 8:
                    print("", end="| ")
            print()
            if self.sudokuMatrix.index(row) == 2 or self.sudokuMatrix.index(row)==5 or self.sudokuMatrix.index(row)==8:
                print(" -----------------------")


class constraint(sudoku, ABC):
    @abstractmethod
    def checkViolation(self):
        pass            


class sudokuRow(constraint):
    

    def __init__(self, index):
        self.index = index
        self.containedCells = []

    def addCell(self, cell):
        self.containedCells.append(cell)
        print

    def checkViolation(self):
        seen = []
        for cell in self.containedCells:
            if cell.value in seen and cell.value != -1:
                return True
            else:
                seen.append(cell.value)
        return False


class sudokuColumn(constraint):


    def __init__(self, index):
        self.index = index
        self.containedCells = []

    def addCell(self, cell):
        self.containedCells.append(cell)

    def checkViolation(self):
        seen = []
        for cell in self.containedCells:
            if cell.value in seen and cell.value != -1:
                return True
            else:
                seen.append(cell.value)
        return False

class sudokuBox(constraint):

    def __init__(self, index):
        self.index = index
        self.containedCells = []

    def addCell(self, cell):
        self.containedCells.append(cell)

    def checkViolation(self):
        seen = []
        for cell in self.containedCells:
            if cell.value in seen and cell.value != -1:
                return True
            else:
                seen.append(cell.value)
        return False

    

class cell(sudokuRow, sudokuColumn, sudokuBox):
    appliedConstraints = []
    def __init__(self, value, sudokuRow, sudokuColumn, sudokuBox):
        self.value = value
        self.sudokuRow = sudokuRow
        self.sudokuColumn = sudokuColumn
        self.sudokuBox = sudokuBox
        self.sudokuRow.addCell(self)
        self.sudokuColumn.addCell(self)
        self.sudokuBox.addCell(self)
        self.appliedConstraints.append(sudokuRow)
        self.appliedConstraints.append(sudokuColumn)
        self.appliedConstraints.append(sudokuBox)

def createEmpty():
    emptySudoku = sudoku()
    matrix = []
    for row in range(9):
        matrixRow = []
        for col in range(9):
            box = getBox(row, col)
            cellRow = emptySudoku.findRow(row)
            cellColumn = emptySudoku.findColumn(col)
            cellBox = emptySudoku.findBox(box)
            newCell = cell(-1, cellRow, cellColumn, cellBox)
            matrixRow.append(newCell)
        matrix.append(matrixRow)
    emptySudoku.sudokuMatrix = matrix
    return emptySudoku

def hey():
    print("hey")

# class sudokuArrow(constraint):
#     sum = 0
#     sumCell = cell()
#     lineCells = []
#     def __init__(self):
#         pass
#     def get(self):
#         return self
#     def addArrowCell(self, arrowCell):
#         arrowCellType = arrowCell.getType()
#         if arrowCellType == "line":
#             self.lineCells.append(arrowCell)
#         else:
#             self.sumCell = arrowCell

#     def checkViolation(self):
#         total = 0
#         complete = True
#         for cell in self.lineCells:
#             if cell.value != -1:
#                 complete = False
#             else:
#                 total = total+cell.value
#         if complete and self.sum != total:
#             return True
#         elif not complete and self.sum < total:
#             return True
#         else:
#             return False
            


# class arrowCell(sudokuArrow, cell):
#     def __init__(self, sudokuArrow, type):
#         self.sudokuArrow = sudokuArrow
#         self.type = type


# def newSudoku():
    # for row in range(9):
    #     newRow = sudokuRow()
    #     for col in range(9):
    #       newColumn = sudokuColumn()
    #     newBox = sudokuBox()

    

# class cell:
#     def __init__(self, value, row, column, box):
#         self.value = value
#         self.row = row
#         self.column = column
#         self.box = box

# def convertToCells(matrix):
#     convertedSudoku = []
#     for row in range(9):
#         convertedRow =[]
#         for col in range(9):
#             box = -1
#             if row < 3:
#                 if col < 3:
#                     box = 0
#                 elif col < 6:
#                     box = 1
#                 else:
#                     box = 2

#             elif row < 6:
#                 if col < 3:
#                     box = 3
#                 elif col < 6:
#                     box = 4
#                 else:
#                     box = 5
#             else:
#                 if col < 3:
#                     box = 6
#                 elif col < 6:
#                     box = 7
#                 else:
#                     box = 8

#             newCell = cell(matrix[row][col], row, col, box)
#             convertedRow.append(newCell)
#         convertedSudoku.append(convertedRow)
#     return convertedSudoku

def convertToCells(matrix):
    convertedSudoku = sudoku()
    sudokuMatrix = []
    for row in range(9):
        matrixRow = []       
        for col in range(9):
            box = getBox(row, col)
            cellRow = convertedSudoku.findRow(row)
            cellColumn = convertedSudoku.findColumn(col)
            cellBox = convertedSudoku.findBox(box)
            newCell = cell(matrix[row][col], cellRow, cellColumn, cellBox)
            # cellRow.addCell(newCell)
            # cellColumn.addCell(newCell)
            # cellBox.addCell(newCell)
            matrixRow.append(newCell)
        sudokuMatrix.append(matrixRow)
    convertedSudoku.sudokuMatrix = sudokuMatrix
    return convertedSudoku


def getBox(row, col):
    if row < 3:
        if col < 3:
            return 0
        elif col < 6:
            return 1
        else:
            return 2
    elif row < 6:
        if col < 3:
            return 3
        elif col < 6:
            return 4
        else:
            return 5
    else:
        if col < 3:
            return 6
        elif col < 6:
            return 7
        else:
            return 8



# def printSudoku(sudoku):
#     print(" ----------------------")
#     for i in sudoku:
#         for j in i:
#             if j.sudokuColumn.index == 0 or j.sudokuColumn.index == 3 or j.sudokuColumn.index == 6: 
#                 print("", end="| ")
#             if j.value == -1:
#                 print("x", end=" ")
#             else:
#                 print(j.value , end=" ")
#             if j.sudokuColumn.index == 8:
#                 print("", end="| ")

#         print()
#         if sudoku.index(i) == 2 or sudoku.index(i)==5 or sudoku.index(i)==8:
#             print(" -----------------------")

# def printSudoku(sudoku):
#     print(" ----------------------")



#     for i in sudoku:
#         for j in i:
#             if j.sudokuColumn.index == 0 or j.sudokuColumn.index == 3 or j.sudokuColumn.index == 6: 
#                 print("", end="| ")
#             if j.value == -1:
#                 print("x", end=" ")
#             else:
#                 print(j.value , end=" ")
#             if j.sudokuColumn.index == 8:
#                 print("", end="| ")

#         print()
#         if sudoku.index(i) == 2 or sudoku.index(i)==5 or sudoku.index(i)==8:
#             print(" -----------------------")

def printCell(cell):
    print("Value: " + str(cell.value))
    print("Row: " + str(cell.row))
    print("Column: " + str(cell.column))
    print("Box: " + str(cell.box))


def checkConstraints(sudoku):
    for row in sudoku.sudokuMatrix:
        for col in row:
            if col.sudokuRow.checkViolation():
                return True
            if col.sudokuColumn.checkViolation():
                return True
            if col.sudokuBox.checkViolation():
                return True
    return False



def checkBranch(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku.sudokuMatrix[row][col].value == -1:
                for x in range(9):
                    # print("-")
                    # print(x+1)
                    # print("-")
                    newSudoku = copy.deepcopy(sudoku)
                    newSudoku.sudokuMatrix[row][col].value = x+1
                    # printSudoku(newSudoku)
                    if not checkConstraints(newSudoku):
                        if checkIfSolved(newSudoku):
                            newSudoku.printSudoku()
                            return True 
                        if checkBranch(newSudoku):
                            return True
                sudoku.sudokuMatrix[row][col].value = -1
                return False    
                
                    
                    
        
def checkIfSolved(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku.sudokuMatrix[row][col].value == -1:
                return False
            if checkConstraints(sudoku):
                return False
    return True



# celledSudoku = convertToCells(puzzle)
# printSudoku(celledSudoku)
# print("Solved?")
# print(checkIfSolved(celledSudoku))

# print(checkBranch(celledSudoku))
# executionTime = time.time() - startTime
# print("Solution was found in " + str(executionTime) + " seconds")
def run():
    exampleSudoku = convertToCells(puzzle)
    exampleSudoku.printSudoku()
    print(checkConstraints(exampleSudoku))
    print("Solved?")
    print(checkIfSolved(exampleSudoku))
    checkBranch(exampleSudoku)