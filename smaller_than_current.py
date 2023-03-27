"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
"""


def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    sorted_nums = sorted(nums)
    mapping = {}

    for idx, num in enumerate(sorted_nums):
        if num not in mapping:
            mapping[num] = idx

    return [mapping[num] for num in nums]