"""
Given a string s of zeros and ones, return the maximum score after splitting 
the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus 
the number of ones in the right substring.

EXPLANATION:

The most important hint is to first count the number of '1's in the string, if we know that
we can just traverse the string from left to right and keep track of our best result so far.
"""

def maxScore(s: str) -> int:
    score = s.count("1")
    best = 0
    
    for i in range(len(s) - 1):
        if s[i] == "1":
            score -= 1
        else:
            score += 1

        best = max(best, score)
        
    return best