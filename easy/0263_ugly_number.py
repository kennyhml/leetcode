"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

EXPLANATION:

So here I had some reading up to do, as a reminder a prime number is a number that is only divisible by 1
or itself. The prime factors of a number are the primes used to make the number.


The prime factorisation of 24 gives 2 x 2 x 2 x 3 = 23 x 3, where 2 and 3 are the prime factors of 24

To compute the prime factors, for a number n, we divide n by a factor until it is no longer evenly divisible,
while keeping track of the number of divisions, then move on to the next prime.
"""


def isUgly(n: int) -> bool:
    if n <= 0: # numbers < 2 have no prime factors
        return False
        
    for prime in (2, 3, 5):
        while n % prime == 0:
            n //= prime

    return n == 1 # if n is 1 now then all factors are exhausted, otherwise theres more
