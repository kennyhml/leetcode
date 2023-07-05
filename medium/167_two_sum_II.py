"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers be 
numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.


EXPLANATION:

Use a low and a high pointer, since the array is sorted, if the current sum of the two pointers is bigger
than the target, we shift the high pointer to the left, otherwise we shift our low pointer to the right.

There is guaranteed to be a match.

Not sure how this is supposed to be a medium problem...
"""


def twoSum(numbers: list[int], target: int) -> list[int]:
    low = 0
    high = len(numbers) - 1

    while high > low:
        curr_sum = numbers[low] + numbers[high]
        if curr_sum == target:
            return [low + 1, high + 1]

        if curr_sum > target:
            high -= 1
        else:
            low += 1
            