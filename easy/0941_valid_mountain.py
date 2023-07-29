"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


Doesnt need an explanation imo lol.
"""

def validMountainArray(arr: list[int]) -> bool:
    increased = decreased = False
    n = len(arr)
    
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            return False
        elif arr[i] < arr[i - 1]:
            if not increased:
                return False
            decreased = True
        else:
            if decreased:
                return False
            increased = True
            
    return increased and decreased