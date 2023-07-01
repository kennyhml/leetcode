"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and 
grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely 
surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around 
the island. One cell is a square with side length 1. The grid is rectangular, width and height don't 
exceed 100. Determine the perimeter of the island."""



def islandPerimeter(grid: list[list[int]]) -> int:
    perimeter = 0

    for idx, row in enumerate(grid):
        for i, field in enumerate(row):
            if not field:
                continue
        
            if not idx or not grid[idx - 1][i]:
                perimeter += 1

            if not i or not grid[idx][i-1]:
                perimeter += 1
            
            if i == len(row) - 1 or not grid[idx][i + 1]:
                perimeter += 1
            
            if idx == len(grid) - 1 or not grid[idx + 1][i]:
                perimeter += 1

    return perimeter