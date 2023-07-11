"""
You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

"""


import itertools

def mergeAlternately(word1: str, word2: str) -> str:

    res = ""
    zipped = itertools.zip_longest(word1, word2)

    for i, (a, b) in enumerate(zipped):
        if a is None or b is None:
            return res + (word1[i:] if b is None else word2[i:])
        res += a
        res += b


    return res