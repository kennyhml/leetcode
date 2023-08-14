"""
You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.

For example, in the string "(name)is(age)yearsold", there are two bracket pairs that contain 
the keys "name" and "age".
You know the values of a wide range of keys. This is represented by a 2D string array knowledge where each 
knowledge[i] = [keyi, valuei] indicates that key keyi has a value of valuei.

You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains
some key keyi, you will:

Replace keyi and the bracket pair with the key's corresponding valuei.
If you do not know the value of the key, you will replace keyi and the bracket pair with a 
question mark "?" (without the quotation marks).
Each key will appear at most once in your knowledge. There will not be any nested brackets in s.

Return the resulting string after evaluating all of the bracket pairs.

EXPLANATION:

Pretty simple problem, first we turn our knowledge data into a hashtable, otherwise we keep having O(n) lookup
when it could just be O(1) in turn for O(n) extra space. 

Once thats done we just need to walk through our string while we create a new string and be logical about the
steps. I personally like to use a variable that serves as a flag whether we are currently inside a bracket or 
not, and then base the logic on that.
"""


def evaluate(s: str, knowledge: list[list[str]]) -> str:
    data = dict(knowledge)
    curr = res = ""
    bracket = False

    for c in s:
        if c == ")":
            res += data.get(curr, "?")
            curr, bracket = "", False
        elif bracket:
            curr += c
        elif c == "(":
            bracket = True
        else:
            res += c

    return res
