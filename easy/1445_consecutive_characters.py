"""
The power of the string is the maximum length of a non-empty substring 
that contains only one unique character.

Given a string s, return the power of s
"""

def maxPower(s: str) -> int:
    best = streak = 1
    previous = ""

    for char in s:
        if char == previous:
            streak += 1
            best = max(best, streak)
        else:
            streak = 1
        previous = char
    
    return best

