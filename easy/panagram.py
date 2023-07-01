"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
"""


def checkIfPangram(sentence: str) -> bool:

    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    for c in sentence:
        if c in alphabet:
            alphabet.remove(c)
            if not alphabet:
                return True
    return False