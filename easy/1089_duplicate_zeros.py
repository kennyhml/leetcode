"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, 
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. 
Do the above modifications to the input array in place and do not return anything.

EXPLANATION:

Ugly solutions such as O(n^2) solutions do pass, just not efficient at all. The right approach is to
consider how many values we are going to have shifted, i.e if we have 3 zeros in the array, we know
that the resulting array would be n + 3 long where n is the original length of the array, but we need
to keep the array at its original size and drop exceeding values.

So we iterate over the array in reverse, if our current index + the number of zeros to duplicate left
doesnt exceed our array size we can put our value there. If we hit a 0 we can remove that from our 0
count and duplicate it (granted it fits into the array).
"""

def duplicateZeros(arr: list[int]) -> None:
    zeros, n = arr.count(0), len(arr)

    for i in range(n - 1, -1, -1):
        if i + zeros < n:
            arr[i + zeros] = arr[i]

        if arr[i] == 0:
            zeros -= 1
            if i + zeros < n:
                arr[i + zeros] = 0