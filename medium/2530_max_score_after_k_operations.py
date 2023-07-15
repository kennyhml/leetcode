"""
You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:

choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.

The ceiling function ceil(val) is the least integer greater than or equal to val.

EXPLANATION:

The difficulty here is really just making it efficient, we could do it with native datatypes but it doesnt
pass the tests because it times out, i.e getting the biggest number for every iteration.

Thats why for efficiency purposes we have to use a heap, a heap uses an underlying binary tree structure
to store the elements priorities. But heaps are implemented as minheaps, how do we use it as maxheap?

Easy, we just turn every number into its negative counterpart and then create the heap for that, when we pop
an element we revert it back into the positive number and when we push an element we use its negative version.

With knowledge about heaps in mind it might as well be an easy question.

For optimizatio purposes, since the restrictions say that 1 <= nums[i] <= 109 (each number is between 1 and 109),
if our biggest number turns out to be 1, we know that all other numbers will also be no bigger than 1 and never smaller
because math.floor(1 / 3) will still be 1.

So we can just stop adding up our scores and add the remaining iterations to the score.
"""

import math
import heapq

def maxKelements(nums: list[int], k: int) -> int:
    nums = [-num for num in nums]
    heapq.heapify(nums)
    i = score = 0

    while i < k:
        biggest = -heapq.heappop(nums)
        if biggest == 1:
            break

        score += biggest
        decreased = math.ceil(biggest / 3)
        heapq.heappush(nums, -decreased)
        i += 1

    return score + (k - i)