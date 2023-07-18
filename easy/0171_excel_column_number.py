"""
Given a string columnTitle that represents the column title as 
appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

EXPLANATION:

Its very similar to converting a base26 number, just that we dont use 0-25 but 1-26. So each value is

ch * (26 ^ n - 1) , where n = length of the given string and ch is the position of the character in the alphabet.

Since our n starts at 0 rather than 1 we dont need the -1
"""



class Solution:
    alphabet = {}
    for i in range(26):
        letter = chr(i + 65)
        alphabet[letter] = i + 1

    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i, char in enumerate(reversed(columnTitle)):
            res += self.alphabet[char] * (26 ** i)

        return res