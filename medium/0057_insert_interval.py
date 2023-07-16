"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals 
still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.


EXPLANATION:

We need to realize the following things:

- If the start of the interval is greater than the end of our new interval, we need to insert it and return, no merge
- If the end of the interval is smaller than the start of our new interval, there is no merge so we just add the interval
- When we merge an interval with our new interval, the start will be the min of both and the end will be the max of both
"""


def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    result = []
    
    for i, (start, end) in enumerate(intervals):
        new_start, new_end = newInterval
        if start > new_end:
            result.append(newInterval)
            return result + intervals[i:]
        elif end < new_start:
            result.append(intervals[i])
        else:
            newInterval = [min(start, new_start), max(end, new_end)]
    
    result.append(newInterval)
    return result