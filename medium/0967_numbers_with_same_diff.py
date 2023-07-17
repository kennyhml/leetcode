"""
Given two integers n and k, return an array of all the integers of length n where the difference 
between every two consecutive digits is k. You may return the answer in any order.

Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.


EXPLANATION:


Get the numbers that are valid to be used, then use a recursive approach to generate all possible 
combinations and add them to the array. We stop our recursive generation when num has more than n digits.
"""


def numsSameConsecDiff(n: int, k: int) -> list[int]:

    valid = {i for i in range(10) if i + k < 10 or 0 <= i - k < 10}
    limit = 10 ** (n - 1)
    res = []

    def generate(num):
        last = num % 10
        
        if num >= limit:
            res.append(num)
            return

        up, down, scaled = last + k, last - k, num * 10
        
        if up in valid:
            generate(scaled + up)
            
        if down in valid and up != down:
            generate(scaled + down)
            
    for num in valid:
        if num != 0:
            generate(num)

    return res