"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

EXPLANATION:

I think this problem was quite easy so there isnt much explanation needed. The problem requires us to return 0 if
number can not be represented in 32bit, 32 bit is just (2 ** 31) - 1, do take note of the -1, it would be 33bit without.

This goes both ways, so it can also not be 'smaller' than -2 ** 31, I simply use `abs` to check both in one condition.
"""

def reverse(x: int) -> int:
    maxsize= (2 ** 31) - 1
    if abs(x) > maxsize:
        return 0
        
    negative = x < 0
    if not negative:
        num = int(str(x)[::-1])
    else:
        num = 0 - int(str(x)[:0:-1])

    return 0 if abs(num) > maxsize else num