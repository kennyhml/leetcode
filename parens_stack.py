"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""

def is_valid(s: str) -> bool:

    parens = ["(", ")", "[", "]", "{", "}"]
    closers = {")": "(", "}": "{", "]": "["}
    stack = []

    for c in s:
        if c not in parens:
            continue

        if not stack and c in closers:
            return False
        
        if not c in closers:
            stack.append(c)

        elif c in closers:
            if stack.pop() != closers[c]:
                return False
            
    return not stack