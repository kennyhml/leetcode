"""
Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:

- nums[a] + nums[b] + nums[c] == nums[d], and
- a < b < c < d

EXPLANATION:

The solution basically just asks for a brute force since the constraints are pretty limited.
"""

def countQuadruplets(nums: list[int]) -> int:
    
    n = len(nums)
    count = 0

    for a in range(n - 3):
        for b in range(a + 1, n - 2):
            for c in range(b + 1, n - 1):
                for d in range(c + 1, n):
                    if nums[a] + nums[b] + nums[c] == nums[d]:
                        count += 1

    return count