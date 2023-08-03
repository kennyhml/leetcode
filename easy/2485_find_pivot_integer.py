"""
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all 
elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is 
guaranteed that there will be at most one pivot index for the given input.
"""

def pivotInteger(n: int) -> int:


    total = sum(range(n + 1))
    left = 0
    for num in range(n + 1):
        left += num
        if left == total:
            return num
        total -= num

    return -1