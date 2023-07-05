"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such
that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


We have to treat this as combination of two sum 1 and two sum 2, we essentially use the two_sum_II
algorithm on the right side of the array.
"""


def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    ret = []

    for idx, a in enumerate(nums):
        if idx > 0 and nums[idx - 1] == a or a > 0:
            continue

        low = idx + 1
        high = len(nums) - 1

        while high > low:
            _sum = a + nums[low] + nums[high]
            if _sum < 0:
                low += 1
            elif _sum > 0:
                high -= 1
            else:
                ret.append([a, nums[low], nums[high]])
                low += 1
                while nums[low] == nums[low - 1] and low < high:
                    low += 1

    return ret
