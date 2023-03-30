"""
You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.
"""
def differenceOfSum(nums: list[int]) -> int:

    dsum = 0
    for num in nums:
        if num < 10:
            dsum += num
        else:
            dsum += sum(int(c) for c in str(num))

    return sum(nums) - dsum