"""
Given a string s containing only lowercase English letters and the '?' character, 
convert all the '?' characters into lowercase letters such that the final string 
does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. 
If there is more than one solution, return any of them. It can be shown that an 
answer is always possible with the given constraints.
"""

def modifyString(s: str) -> str:
    s = list(s)

    def find_char(l, r):
        for o in range(97, 100):
            if (l and l - 1 < o < l + 1) or (r and r - 1 < o < r + 1):
                continue

            return chr(o)
            
    for i, char in enumerate(s):
        if char != "?":
            continue

        left = ord(s[i - 1]) if i > 0 else None
        right = ord(s[i + 1]) if i < len(s) - 1 else None
        s[i] = find_char(left, right)

    return "".join(s)