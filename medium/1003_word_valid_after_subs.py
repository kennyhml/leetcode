"""
Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "", you can transform t 
into s after performing the following operation any number of times:

Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, 
where t == tleft + tright. Note that tleft and tright may be empty.

Return true if s is a valid string, otherwise, return false.

EXPLANATION:

We can use a stack to keep track of the recent characters, if the stack doesnt at least have 2 characters
or doesnt pop a b and then an a when we encounter a c, if we can conclude that it is invalid.
"""

def isValid(s: str) -> bool:
    stack = []

    for c in s:
        if c != 'c':
            stack.append(c)
        elif len(stack) < 2 or stack.pop() != 'b' or stack.pop() != 'a':
            return False
    
    return not stack

def isValid(s: str) -> bool:
    """Another solution, more cheesy.

    Faster but only because of pythons builtins being optimized in c.
    """
    while s:
        previous_length = len(s)
        s = s.replace("abc", "")
        
        if len(s) == previous_length:
            return False

    return True