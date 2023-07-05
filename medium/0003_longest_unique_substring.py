"""Given a string s, find the length of the longest substring without repeating characters.


EXPLANATION:

The important thing here was to realize that when we found the end of a substring without repeating
characters, we cannot just start looking at the next substring from here. Instead, we have to walk back
to the last occurrence of the character that 'broke' the substring.


Take 'dvdf' as example, if we walk like: d -> v -> d and break here because of a repeated d, it might seem right
to go on like d -> f, but notice how we never took v -> d -> f into consideration here.

The easiest way is to walk backwards, but that can be kinda slow right, right?

If only there was a quick and easy way to remember where we saw the last occurrence of x character...
thats right, we just throw a hasmap at it!

As we go we essentially remember where we saw what character last, and then just take a step back to it.
"""

def lengthOfLongestSubstring(s: str) -> int:
    start = longest = 0
    seen = {}

    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        else:
            longest = max(longest, i - start + 1)
        
        seen[char] = i

    return longest