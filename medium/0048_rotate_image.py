"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

EXPLANATION:

So yea this question was tough primarly because of the fact that we first need to find the right pattern
to approach this and then also consider how we preserve the value we replace.

I will show 3 different solutions from easy to more complex, but also least efficient to most efficient.
"""



def rotate(matrix: list[list[int]]) -> None:
    """This is kind of a cheese solution and not very efficient, we iterate
    over the rows in reverse and pop the 4 elements off the row, and then append
    them to the rows where they should be, meaning there will temporarily be more
    values in certain rows, not the expected 4. They will be popped off when the
    algorithm gets there."""

    n = len(matrix)
    for row in reversed(matrix):
        for i in range(n):
            element = row.pop(0)
            matrix[i].append(element)


def rotate(matrix: list[list[int]]) -> None:
    """Here it gets a little more complex, we essentially iterate over the rows
    and all columns after the rows index, the reason this works is considering we
    have an element at i, j of 1, 0, then we need to swap this element with the
    element at j, i or 0, 1 to successfully rotate our matrix.

    Meaning the element at matrix[i][j] ends up being matrix[j][i] and vice versa
    """

    n = len(matrix)
    for row in range(n):
        for col in range(row + 1, n):
            matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
        matrix[row].reverse()


def rotate( matrix: list[list[int]]) -> None:
    """The most efficient solution, its time complexity is O(n^2) which is the
    best you can get for rotating a matrix since it involves checking every element
    at least once.
    
    The concept is to keep track of a left and right pointer which also server as top
    and bottom pointers, since its n x n matrix.

    We then just swap our top left value with our bottom left value, the bottom left with the
    bottom right, that one with the top right and that one with the top left.

    Why do we do it in reverse order? Because that way we only have to keep track of a temp
    once we start.

    We could also not use a single temp variable because of how python supports swapping but
    its harder to read.
    """
    n = len(matrix)
    l, r = 0, n - 1

    while l < r:
        top, bottom = l, r
        for i in range(r - l):
            tmp = matrix[top][l + i]
            matrix[top][l + i] = matrix[bottom - i][l]
            matrix[bottom - i][l] = matrix[bottom][r - i]
            matrix[bottom][r - i] = matrix[top + i][r]
            matrix[top + i][r] = tmp

        r -= 1
        l += 1


