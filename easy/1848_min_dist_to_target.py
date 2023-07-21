"""
Given an integer array nums (0-indexed) and two integers target and start, find an 
index i such that nums[i] == target and abs(i - start) is minimized. Note that 
abs(x) is the absolute value of x.

Return abs(i - start).

It is guaranteed that target exists in nums.
"""


def getMinDistance(nums: list[int], target: int, start: int) -> int:
    possible = set()

    for i, num in enumerate(nums):
        if num == target:
            possible.add(i)

    return min(abs(x - start) for x in possible)

    