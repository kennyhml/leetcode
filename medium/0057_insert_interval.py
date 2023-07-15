"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals 
still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""


def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    new_start, new_end = newInterval
    result = []
    inserted = False

    for start, end in intervals:
        if inserted or end < new_start:
            result.append([start, end])
        elif start > new_end:
            result.append([new_start, new_end])
            result.append([start, end])
            inserted = True
        else:
            new_start = min(start, new_start)
            new_end = max(end, new_end)

    if not inserted:
        result.append([new_start, new_end])

    return result