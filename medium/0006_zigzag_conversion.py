"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
"""


def convert(s: str, n: int) -> str:
    """My initial soltuion I came up with without looking at any hints.
    The problem is that its O(n * m) where n is the len(s) and m is n.
    """
    res = [[] for _ in range(n)]
    i = 0
    
    while i < len(s):
        for row in res:
            if i >= len(s):
                return "".join(''.join(c for c in row) for row in res)

            row.append(s[i])
            i += 1

        for idx, row in enumerate(reversed(res)):
            if idx in (range(1, n - 2 + 1)):
                if i >= len(s):
                    return "".join(''.join(c for c in row) for row in res)
                row.append(s[i])
                i += 1
            else:
                row.append("")
                
    return "".join(''.join(c for c in row) for row in res)
    

def convert(s: str, n: int) -> str:
    """The revised solution"""
    if n == 1 or len(s) <= n:
        return s
    
    rows = ['' for _ in range(n)]
    index, step = 0, 1
    
    for char in s:
        rows[index] += char
        
        if index == 0:
            step = 1
        elif index == n - 1:
            step = -1
            
        index += step
    
    return ''.join(rows)

