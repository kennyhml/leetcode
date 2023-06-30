"""
Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.

Return an integer denoting the sum of all numbers in the given range satisfying the constraint.
"""

def sumOfMultiples(n: int) -> int:

    count = 0
    for num in range(1, n+1):
        if any(num % val == 0 for val in (3, 5, 7)):
            count += num
    return count