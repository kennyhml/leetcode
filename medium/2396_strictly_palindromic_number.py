"""
An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

Given an integer n, return true if n is strictly palindromic and false otherwise.

A string is palindromic if it reads the same forward and backward.


There is two solutions for this problem, looking at the constraints: 4 <= n <= 10**5 we can conclude that 
it is impossible for any of the numbers to be palindromic because when we convert any number to the n - 2 base it will
be 12 aside from 4 which is stll not going to be a palindrome.

For example 
    5 in base 3 is 12
    7 in base 5 is 12
    9 in base 7 is 12

    4 in base 2 is 100

So both of these solutions work
"""


class ProperSolution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in (2, (n-2) + 1):
            if not self.is_palindrome(n, base):
                return False
        return True

    def is_palindrome(self, num, base):
        temp = ""
        while num:
            temp += str(num % base)
            if num // base in range(0, base):
                temp += str(num // base)
            num //= base

        return temp[::-1] == temp
    

class Cheesy:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False

