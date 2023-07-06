"""
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

"""

from typing import Optional


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        idx = self.binary_search(nums, target)
        if idx is None:
            return -1, -1

        l = r = idx
        while l >= 0 and nums[l] == target:
            l -= 1

        while r < len(nums) and nums[r] == target:
            r += 1

        return l + 1, r - 1

    def binary_search(self, arr, target) -> Optional[int]:
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (r + l) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1