"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.
"""

def balancedStringSplit(s: str) -> int:
    low = 0
    high = 2
    total = 0

    while high <= len(s):
        sliced = s[low:high]

        if sliced.count("L") != sliced.count("R"):
            high += 2
            continue
        total += 1
        low = high
        high += 2

    return total