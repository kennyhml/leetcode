
"""Given an integer x, return true if x is a palindrome, and false otherwise."""

def ispalindrome(x):
    if isinstance(x, int):
        x = str(x)
    
    if len(x) < 2:
        return True
    
    if x[0] == x[-1]:
        return ispalindrome(x[1:-1])
    return False