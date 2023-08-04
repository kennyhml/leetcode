"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

def setZeroes(matrix: list[list[int]]) -> None:
    columns = set()
    rows = set()

    m = len(matrix)
    n = len(matrix[0])

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                rows.add(row) 
                columns.add(col)

    for row in range(m):
        for col in range(n):
            if col in columns or row in rows:
                matrix[row][col] = 0