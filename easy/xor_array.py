"""
You are given an integer n and an integer start.

Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
"""

def xorOperation(n: int, start: int) -> int:

    arr = [start + 2 * i for i in range(n)]
    
    ret = 0
    for num in arr:
        ret ^= num
    return ret