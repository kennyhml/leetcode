"""
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
"""

def reverseOnlyLetters(s: str) -> str:
    letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    l, r = 0, len(s) - 1
    res = list(s)

    while l < r:
        if not res[l] in letters:
            l += 1

        elif not res[r] in letters:
            r -= 1

        else:
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1
            
    return ''.join(res)