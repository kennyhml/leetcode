"""
Implement the class SubrectangleQueries which receives a rows x cols rectangle as a
matrix of integers in the constructor and supports two methods:

1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)

Updates all values with newValue in the subrectangle whose upper left coordinate is 
(row1,col1) and bottom right coordinate is (row2,col2).
2. getValue(int row, int col)

Returns the current value of the coordinate (row,col) from the rectangle.
"""

class SubrectangleQueries:

    def __init__(self, rectangle: list[list[int]]):
            self.rect = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        
        for row in range(row1, row2+ 1):
            for col in range(col1, col2 + 1):
                self.rect[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rect[row][col]