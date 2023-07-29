"""
ou are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

EXPLANATION:

Use a heapq for efficiency, since we need a maxheap we need to turn the values into their negative counterparts.
"""

import heapq

def lastStoneWeight(stones: list[int]) -> int:
    stones = [-stone for stone in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        largest, second_largest = heapq.nsmallest(2, stones)
        largest, second_largest = -largest, -second_largest

        heapq.heappop(stones)
        heapq.heappop(stones)

        if largest != second_largest:
            heapq.heappush(stones, -(largest - second_largest))

    return -stones[0] if stones else 0