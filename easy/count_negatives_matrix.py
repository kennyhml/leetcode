"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, 
return the number of negative numbers in grid.


Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
"""

def countNegatives(grid: list[list[int]]) -> int:
    count = 0
    n = len(grid[0])

    negatives_only = False

    for row in grid:
        if negatives_only:
            count += n
            continue

        negatives = 0 
        for num in row:
            if num < 0:
                count += 1
                negatives += 1

        if negatives == n:
            negatives_only = True

    return count