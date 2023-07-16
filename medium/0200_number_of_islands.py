"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume a
all four edges of the grid are all surrounded by water.

EXPLANATION:

The hardest part is figuring out how we 'explore' the entire connected island once we hit a "1", for that we can just
recursively "erase" the island into all directions.

I think this was a really simple problem and not much explanation is needed at all.
"""


def numIslands(grid: list[list[str]]) -> int:
    count = 0
    m, n = len(grid), len(grid[0])

    def fill(i, j):
        if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
            grid[i][j] = "0"
            fill(i - 1, j)
            fill(i + 1, j)
            fill(i, j - 1)
            fill(i, j + 1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                count += 1
                fill(i, j)

    return count