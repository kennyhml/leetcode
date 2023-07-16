"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented 
into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

EXPLANATION:

We use memoization to store whether an index in the string can be segmented into words from the dictionary
in shape of a list, we then iterate over every index in the string excluding the first one, and including
the very last one. Our goal is to see whether given the index i, we can find a word with the length l so that
input[i - k:i] is equal to the word, meaning that the segment ending at 1 can be split into a word. 

At the end we just check whether our last index can be segmented, which it only can if the entire string
was segmented.
"""

def wordBreak(s: str, wordDict: list[str]) -> bool:

    # compute length here so we dont need to do it every time
    words = {word: len(word) for word in wordDict}

    n = len(s)
    memo = [False] * (n + 1)
    memo[0] = True # s[:0] is an empty string so we can consider it segmented

    for i in range(1, n + 1):
        for word, length in words.items():

            # Check that the substring fits, is the same, and the start is segmented
            if length <= i and s[i - length:i] == word and memo[i - length]:
                memo[i] = True
                break
                
    return memo[-1]