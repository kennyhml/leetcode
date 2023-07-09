"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.


EXPLANATION:

Simple enough, we can sort the array and then check what n should be, then iterate over the numbers
in the range of n and check whether the number in the array matches, if not we know that the current
number is missing.

If we dont hit the missing number in the loop we know its n thats missing.


But there actually is a much better way to solve it using gaus formula:

Gaus formula says that the sum of all numbers from 0 to n is (n * (n + 1)) // 2

Thus we can quickly calculate the expected sum given the range and subtract it from our current array
sum, the result will be the number that is missing.
"""


def iterative(nums: list[int]) -> int:

    nums.sort()
    n = len(nums)
    
    for i in range(n):
        if i != nums[i]:
            return i

    return n 


def gaus_formula(nums: list[int]) -> int:
    return (len(nums) * (len(nums) + 1)) // 2 - sum(nums)