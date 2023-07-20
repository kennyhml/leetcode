"""
Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.

EXPLANATION: 

The trick is realizing that to find the divisors of a number, you only need to iterate to the square root of 
that number. If we find a valid division for num + 1 then we dont need to check num + 2 because we know the
absolute difference for num + 1 will be smaller.
"""

def closestDivisors(num: int) -> list[int]:
    target1, target2 = num + 1, num + 2
    sqrt = int(target2 ** 0.5)

    for i in range(sqrt, 0, -1):
        if target1 % i == 0:
            return [i, target1 // i]

        if target2 % i == 0:
            return [i, target2 // i]