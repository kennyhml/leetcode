"""
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

EXPLANATION:

I solved it via binary search first but it wasnt really as fast as expected - then I noticed the problem
really just boils down to good old two sum I, I dont think much explanation is needed based on the code
readability.
"""
def findPairs(nums: list[int], k: int) -> int:
    ret = 0
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1

    for num, occurrences in d.items():
        if k == 0:
            ret += occurrences > 1
        elif num + k in d:
            ret += 1
    return ret