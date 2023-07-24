"""
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest 
of the intervals non-overlapping.

EXPLANATION:

If we sort the intervals by end, we can sorta flip this around, instead of asking how many we have to remove
for it not to overlap, lets ask how many we CAN ATTEND without overlapping instead. At the end we just subtract
that from our total number of intervals and that way we know we have to remove at least that many.
"""

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda interval: interval[1])
    prev, count = 0, 1
    n = len(intervals)

    for i in range(1, n):
        if intervals[i][0] >= intervals[prev][1]:
            prev = i
            count += 1

    return n - count