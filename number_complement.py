"""
The complement of an integer is the integer you get when you flip 
all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.
"""



# I came up with two solutions for this, the first one was using the bit_length to get the bits length, 
# but it felt like cheating cause it is is a builtin


def find_complement_1(num: int) -> int:

    bits = 0
    tmp = num
    
    while tmp != 0:
        tmp = tmp >> 1
        bits += 1
    
    return num ^ 2 ** bits - 1


def find_complement(num: int) -> int:

    return num ^ 2 ** num.bit_length() - 1

