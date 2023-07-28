"""
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] 
is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.

EXPLANATION:

The key to solving this is Kadane's algorithm, which goes as follows:

best = current = 0

for x in arr:
    current = max(0, current + x)
    best = max(best, current)

    
But since we allow a negative value made absolute, we jut need to modify that a tad bit.
"""

def maxAbsoluteSum(nums: list[int]) -> int:
    curr_max = curr_min = res = 0

    for num in nums:
        curr_max = max(0, curr_max + num)
        curr_min = min(0, curr_min + num)

        res = max(res, curr_max, -curr_min)

    return res