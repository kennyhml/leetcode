"""
You have a long flowerbed in which some of the plots are planted, 
and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 
means empty and 1 means not empty, and an integer n, return if n new 
flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        planted = 0

        for idx, flower in enumerate(flowerbed):
            if (
                flower == 1
                or flowerbed[max(0, idx - 1)] == 1
                or flowerbed[min(len(flowerbed) - 1, idx + 1)] == 1
            ):
                continue

            flowerbed[idx] = 1
            planted += 1
            if planted == n:
                return True

        return planted >= n
