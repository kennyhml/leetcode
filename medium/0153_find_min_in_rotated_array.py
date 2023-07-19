"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 

For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

EXPLANATION:

If nums[mid] is bigger than nums[right] we know that we have to be in the left rotated portion of the array, 
as for an array like [4,5,6,7,0,1,2] the only values greater than 2 are 4, 5, 6 and 7 which is the left portion.

In that case, we cross out the left portion and focus on the right, at which point its just a binary search.
"""

def findMin(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2

        # check whether we are in the left portion
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]