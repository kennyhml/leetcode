"""
Given an array of strings patterns and a string word, 
return the number of strings in patterns that exist as a substring in word.

A substring is a contiguous sequence of characters within a string.
"""

def numOfStrings(patterns: list[str], word: str) -> int:
    count = 0
    for pattern in patterns:
        if pattern in word:
            count += 1
    return count