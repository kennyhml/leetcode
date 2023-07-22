"""
You are given two positive integers n and k. A factor of an integer n 
is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the 
kth factor in this list or return -1 if n has less than k factors.
"""


def kthFactor(n: int, k: int) -> int:
    factors = [1]
    count = 2
    while len(factors) != k:
        if count > n:
            return -1
        if n % count == 0:
            factors.append(count)
        count += 1

    return factors[-1]


from math import sqrt

def fasterKthFactor(n: int, k: int) -> int:
    factors = [i for i in range(1, int(sqrt(n)) + 1) if n % i == 0]
    if k <= len(factors):
        return factors[k - 1]
    k += (factors[-1] ** 2) == n
    if k > len(factors) * 2:
        return -1
    k -= len(factors)
    return n // factors[-k]
