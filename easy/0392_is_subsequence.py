"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

def isSubsequence(s: str, t: str) -> bool:
    n, k = len(s), len(t)
    available = set(t)
    i = j = 0

    while i < n:
        if j >= k:
            return False

        target, provided = s[i], t[j]
        if target == provided:
            i += 1; j += 1

        elif target not in available:
            return False
        
        else:
            while j < k and t[j] != target:
                j += 1

    return True