"""
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. 
For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive 
deci-binary numbers needed so that they sum up to n.

Example 1:
    Input: n = "32"
    Output: 3
    Explanation: 10 + 11 + 11 = 32


EXPLANATION:
    This task seems extremely tricky until you notice the extreme simple trick, once you do its simpler than any
    easy question - the minimum number of deci-binary numbers is literally just the biggest digit in the input.


Consider 82734,  we have to add
    11111
    11111
    10111
    10101
    10100
    10100
    10100
    10000

    82734

Which is 8 deci-binary numbers, the biggest digit in the input number.
"""

def minPartitions(n: str) -> int:
    return int(max(n))