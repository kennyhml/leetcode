"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"

"""


def longest_common_prefix(strs: list[str]) -> str:

    prefix = ""
    for char_idx, char in enumerate(strs[0]):
        for other_word in strs:
            try:
                if not other_word[char_idx] == char:
                    return prefix
            except IndexError:
                return prefix
        prefix += char
    
    return prefix