"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

EXPLANATION:

We know that if we have to rotate the array by k places, the new start of the array will be n - k
where n is the length of the array we rotate. For cases where the array has to wrap around multiple
times, we just use k % n so that we only do it once.
"""

def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n
    
    target = n - k
    nums[:] = nums[target:] + nums[:target]
