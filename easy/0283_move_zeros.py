"""
Given an integer array nums, move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


EXPLANATION:

We have a left and a right pointer, the left pointer will always point to our most left zero,
the right pointer will walk through our numbers. If the right pointer is a non zero number while
our left pointer is on a zero, we swap them.


Example:
[0, 1, 0, 3, 12]       [0, 1, 0, 3, 12]       [1, 0, 0, 3, 12]      [1, 0, 0, 3, 12]      [1, 0, 0, 3, 12]
 ↑                ->    ↑  ↑             ->       ↑             ->      ↑  ↑          ->      ↑     ↑
l/r                     l  r                     l/r                    l  r                  l     r
"""


def moveZeroes(nums: list[int]) -> None:
    left = 0
    for right in range(len(nums)):
        if (r := nums[right]) != 0 and nums[left] == 0:
            nums[left], nums[right] = r, 0
            
        if nums[left] != 0:
            left += 1