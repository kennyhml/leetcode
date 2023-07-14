"""
You are given a 0-indexed integer array nums. A pair of indices i, j where 0 <= i < j < nums.length 
is called beautiful if the first digit of nums[i] and the last digit of nums[j] are coprime.

Return the total number of beautiful pairs in nums.

Two integers x and y are coprime if there is no integer greater than 1 that divides both of them. 
In other words, x and y are coprime if gcd(x, y) == 1, where gcd(x, y) is the greatest common divisor of x and y.
"""



import math

def countBeautifulPairs(nums: list[int]) -> int:

    n = len(nums)
    res = 0

    for i in range(n):
        for j in range(i+1, n):
            num1 = int(str(nums[i])[0])
            num2 = nums[j] % 10
            if math.gcd(num1, num2) == 1:
                res += 1
    return res