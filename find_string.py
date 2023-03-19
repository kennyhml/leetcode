"""
Given two strings needle and haystack, return the index of the first 
occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


def strStr(haystack: str, needle: str) -> int:

    frame_start = 0
    frame_end = len(needle)
    idx = 0

    while frame_end <= len(haystack):
        if haystack[frame_start:frame_end] == needle:
            return idx

        idx += 1
        frame_start += 1
        frame_end += 1

    return -1
