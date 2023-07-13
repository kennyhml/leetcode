"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot 
index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index 
of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


EXPLANATION:

We could do two binary searches, one to find the pivot and then another one to search in the correct half
based on where we found the pivot.

However we could also just do it at the same time, as always we initialize a left and right pointer, when
we look at the mid value we need to check whether our leftmost value is smaller or equal to our middle
value, if it is, we know that we have to be on the left side of the pivot, because if our middle value
was smaller it wouldnt be possible that its past the left pointer unless its located in the rotated pivot.


[4, 5, 6, 7, 0, 1, 2]   # 4 is smaller than 7, so we know know that our current
 ↑        ↑        ↑    # mid pointer is located on the left side of the pivot 
 L        M        R    # if there is a pivot in the array.

 
[4, 5, 6, 7, 0, 1, 2]   # Now we check whether left <= target < middle, because if
 ↑        ↑        ↑    # target is within the left and middle values, we know that
 L        M        R    # we only need to continue searching the left half

 
[4, 5, 6, 7, 0, 1, 2]   # Since the left value is biggger than our target 0, the condition
             ↑  ↑  ↑    # did not match and the target is not on the left, so it has to be
             L  M  R    # on the right, meaning we can set our left pointer to be middle + 1
"""

def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] == target:
            return mid

        if nums[l] <= nums[mid]: # our mid pointer is currently in the left section
            if nums[l] <= target < nums[mid]: # our target is inside the left section
                r = mid-1
            else: # Our target is in the right section 
                l = mid+1
        else: # our mid pointer is currently in the right section
            if nums[mid] < target <= nums[r]: # our target is in the right section
                l = mid+1
            else: # our target is in the left section
                r = mid-1

    return -1



