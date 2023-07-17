"""
Given an integer array nums and an integer k, modify the array in the following way:

choose an index i and replace nums[i] with -nums[i].
You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.

EXPLANATION:

Just use a minheap and keep negating the smallest element, that way we get the most optimal
solution.
"""

import heapq

def largestSumAfterKNegations(nums: list[int], k: int) -> int:
    heapq.heapify(nums)

    while k > 0 and nums[0] < 0:
        heapq.heapreplace(nums, -nums[0])
        k -= 1

    if k % 2 != 0:
        heapq.heapreplace(nums, -nums[0])

    return sum(nums)

def largestSumAfterKNegations(nums: list[int], k: int) -> int:
    nums.sort()

    for i in range(len(nums)):
        if nums[i] > 0 or k <= 0:
            break

        nums[i] = -nums[i]
        k -= 1

    nums.sort()
    if k > 0 and k % 2 != 0:
        nums[0] = -nums[0]

    return sum(nums)