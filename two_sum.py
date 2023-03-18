"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

def two_sum(nums: list[int], target: int) -> list[int]:

    found = {}
    for idx, i in enumerate(nums):
        complement = target - i

        if complement in found:
            return [idx, found[complement]]
        
        found[i] = idx

        