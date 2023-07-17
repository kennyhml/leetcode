"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""


from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    a, b = Counter(ransomNote), Counter(magazine)
    return a & b == a