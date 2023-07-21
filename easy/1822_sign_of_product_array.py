"""
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
"""

from math import prod

def arraySign(nums: list[int]) -> int:
    s = prod(nums)
    if s > 0:
        return 1
    elif s < 0:
        return -1
    else:
        return 0