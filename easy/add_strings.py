"""Given two non-negative integers, num1 and num2 represented as string, 
return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers 
(such as BigInteger). You must also not convert the inputs to integers directly.
"""


def add_strings(num1: str, num2: str) -> str:

    if len(num1) < len(num2):
        num1, num2 = num2, num1

    carry = 0
    res: list[str] = []

    for idx, num in enumerate(reversed(num1)):
        try:
            carry, val = divmod(carry + int(num) + int(num2[-idx - 1]), 10)
        except:
            carry, val = divmod(carry + int(num) + 0, 10)
        res.insert(0, str(val))

    if carry:
        res.insert(0, str(carry))

    return "".join(res)
