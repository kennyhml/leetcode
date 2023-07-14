"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of 
bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all 
of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

EXPLANATION:

So it was quite hard to figure out this is actually a binary search problem, the most important
part is understanding what we are binary searching for.

First we need to figure out what the minimimum speed and what the maximum speed is that we can
eat bananas at, then we binary search that range of values until we have found our most efficient
solution.

Example piles = [3, 6, 7, 11], h = 8


First we get the sum of the array, then we find the minimum rate we would need to eat the bananas exactly
within the timeframe, which is the sum of bananas divided by the hours we have, rounded up to the
next integer. In this case it would be math.ceil(27 / 8) which is 4.

Then we calculates the maximum number of bananas that can be eaten per hour to finish within h hours, for 
that we divide the sum by the maximum number of hours that would remain if we distribute one pile per
hour, here it would be math.ceil(27 / (8 - 5 + 1)), so 7.

We know that our target is between 4 and 7 so we start binary searching to find the optimal solution
"""

import math
def minEatingSpeed(piles: list[int], h: int) -> int:
    _sum = sum(piles)

    left = math.ceil(_sum / h)
    right = math.ceil(_sum / (h - len(piles) + 1))
    minimum = right

    def can_eat_within_timeframe(eat_speed):
        taken = 0
        for pile in piles:
            taken += math.ceil(pile / eat_speed)

        return taken <= h
    
    while left <= right:
        mid = (left + right) // 2

        if can_eat_within_timeframe(mid):
            minimum = mid
            right = mid - 1
        else:
            left = mid + 1
    return minimum