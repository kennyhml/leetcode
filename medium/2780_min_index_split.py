"""
An element x of an integer array arr of length m is dominant if freq(x) * 2 > m, where 
freq(x) is the number of occurrences of x in arr. Note that this definition implies 
that arr can have at most one dominant element.

You are given a 0-indexed integer array nums of length n with one dominant element.

You can split nums at an index i into two arrays nums[0, ..., i] and 
nums[i + 1, ..., n - 1], but the split is only valid if:

0 <= i < n - 1
nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant element.
Here, nums[i, ..., j] denotes the subarray of nums starting at index i and 
ending at index j, both ends being inclusive. Particularly, if j < i then 
nums[i, ..., j] denotes an empty subarray.

Return the minimum index of a valid split. If no valid split exists, return -1.

EXPLANATION:

By definition of the dominant element, we know that the dominant element of nums will be the same as the
dominant element of both the splits, meaning rather than trying to find perfect splits, we look at this problem
as trying to balance the occurrences of the dominant element throughout two splits.
"""

def minimumIndex(nums: list[int]) -> int:
    occ = {}
    for num in nums:
        occ[num] = occ.get(num, 0) + 1

    n = len(nums)
    dominant, count = max(occ.items(), key=lambda x: x[1])
    l, r = 0, count

    for i in range(n):
        if nums[i] == dominant:
            l += 1; r -= 1

        j = i + 1
        if l * 2 > j and r * 2 > n - j:
            return i
    return -1