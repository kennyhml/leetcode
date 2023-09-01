"""Given an integer x, return true if x is a palindrome, and false otherwise."""


def ispalindrome(x):
    if isinstance(x, int):
        x = str(x)

    if len(x) < 2:
        return True

    if x[0] == x[-1]:
        return ispalindrome(x[1:-1])
    return False


def isPalindrome(self, s: str) -> bool:
    return (
        all(s[i] == s[~i] for i in range(len(s) // 2))
        if (s := "".join(filter(str.isalnum, s.lower())))
        else False
    )
