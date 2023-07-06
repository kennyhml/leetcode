"""
Given an integer array nums of length n and an integer target, find three integers 
in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.


EXPLANATION:

Works pretty similar to regular 3sum, only difference being that we care about the difference, not the sum.
"""

def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()
    closest = float("inf")

    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            _sum = nums[i] + nums[left] + nums[right]

            curr_diff = abs(target - _sum)
            last_diff = abs(target - closest)

            if curr_diff < last_diff:
                closest = _sum

            if _sum < target:
                left += 1
            elif _sum > target:
                right -= 1
            else:
                return _sum

    return closest