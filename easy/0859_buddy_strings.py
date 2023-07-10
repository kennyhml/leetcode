"""
Given two strings s and goal, return true if you can swap two letters
in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such 
that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

EXPLANATION:

First we check our base cases, i.e if the strings are of different lengths they cant be the same, if they
are the same from the getgo, at least one character must occur twice to make it a buddy string.

Otherwise, we get all pairs of non matching characters, if theres no more than 2 non matching pairs and the
pairs can be swapped, its a buddy string.
"""



def buddyStrings(s: str, goal: str) -> bool:
    n = len(s)
    if n != len(goal):
        return False

    if s == goal:
        return len(set(s)) < n

    differences = [(a, b) for a, b in zip(s, goal) if a != b]
    return len(differences) == 2 and differences[0] == differences[1][::-1]