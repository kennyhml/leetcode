"""
Given an array arr, replace every element in that array with the greatest element among 
the elements to its right, and replace the last element with -1.

After doing so, return the array.

EXPLANATION:

Brute force doesnt pass. Need to realize that we start at the end and keep track of our biggest number yet
when we find a number bigger than it we replace it with our previous max and then start using the new max.
"""


def replaceElements(arr: list[int]) -> list[int]:

    _max = -1
    n = len(arr)

    for i in range(n - 1, -1, -1):
        tmp = arr[i]
        arr[i] = _max
        
        if tmp > _max:
            _max = tmp

    return arr