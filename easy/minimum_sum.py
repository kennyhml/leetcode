"""
You are given a positive integer num consisting of exactly four digits.
Split num into two new integers new1 and new2 by using the digits found in num. 
Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. 
Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.
"""


def minimumSum(num: int) -> int:
    """
    To solve this I had to understand that the first number has to be the smallest
    number + the biggest number, and the second number has to be the remaining 2
    in sorted order.
    """


    nums = [*str(num)]
    nums.sort()

    return int(nums[0] + nums[-1]) + int(nums[1] + nums[2])

