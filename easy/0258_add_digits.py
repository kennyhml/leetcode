"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

EXPLANATION:

Very simple and similar to 'Count digits that divide a number', sure typecasting the integer to a string
and back would work but it would be alot more expensive. Instead we use the same technique to iterate over an
interger, % 10 and then // 10
"""

def addDigits(num: int) -> int:

    while num > 9:
        tmp, n = num, 0
        while tmp:
            n += tmp % 10
            tmp //= 10
        num = n
    return num