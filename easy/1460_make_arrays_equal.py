"""
You are given two integer arrays of equal length target and arr. In one step, 
you can select any non-empty subarray of arr and reverse it. You are 
allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.

EXPLANATION:

This question really teaches you not to overcomplicate things, you can always turn arr into target
so long as target and arr consist of the same values, since we have no restrictions on how many
reverses are allowed, you can always reverse two values to get the target array.
"""

def canBeEqual(target: list[int], arr: list[int]) -> bool:
    return sorted(target) == sorted(arr)