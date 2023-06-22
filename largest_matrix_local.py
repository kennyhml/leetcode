"""
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.
"""


def largestLocal(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid) - 2
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            grid_nums = [row[j:j+3] for row in grid[i:i+3]]
            max_num = max([num for sublist in grid_nums for num in sublist])
            matrix[i][j] = max_num
            
    return matrix