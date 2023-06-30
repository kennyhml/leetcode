"""
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.


EXPLANATION:
--------------

The rules state that if a number is even, you divide it by 2, and if it's odd, you subtract 1 from it.
These operations can be translated into operations on the binary representation:

Dividing an even number by 2 is equivalent to shifting all the bits to the right by 1, discarding the least significant bit.
Subtracting 1 from an odd number is equivalent to changing the rightmost 1-bit to 0 and keeping the remaining bits unchanged.

The binary representation of 14 is 1110, if we divide by 2 thats 7 so 0111.
Now subtracting by 1 would be 6, or 0110

From this we can conclude that for every 1-bit in the binary representation, theres 2 operations:
- Changing the first bit to 0
- Shifting the bits (expect for unit place, which is why we subtract 1 at the end)


For every 0 there is only a single operation which is the right shift.
"""


def numberOfSteps(num: int) -> int:
    binary = bin(num)[2:]
    ones = zeros = 0

    for c in binary:
        if c == "1":
            ones += 1
        else:
            zeros += 1

    return ones * 2 + zeros - 1
