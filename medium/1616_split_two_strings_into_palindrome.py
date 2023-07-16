"""
You are given two strings a and b of the same length. Choose an index and split both strings 
at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, 
and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if 
aprefix + bsuffix or bprefix + asuffix forms a palindrome.

When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. 
For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

Return true if it is possible to form a palindrome string, otherwise return false.

Notice that x + y denotes the concatenation of strings x and y.

EXPLANATION:

Most important part is to realize that we have to find the largest palindromic suffix in a thats a
prefix of b or vice versa. Once we have that we basically know that at least at this point they match
so we can just do the operation and check whether it works out as a palindrome.
"""


def checkPalindromeFormation(a: str, b: str) -> bool:
    n = len(a)

    def palindrome(w) -> bool:
        return w == w[::-1]

    for w1, w2 in ((a, b), (b, a)):
        longest = 0
        for i, char in enumerate(w1, start=1):
            if w2[-i] != char:
                break

            longest += 1
        
        if longest == n:
            return True

        option1 = w1[:longest] + w2[longest:]
        option2 = w1[:-longest] + w2[-longest:]
        if palindrome(option1) or palindrome(option2):
            return True

    return False