"""
I stumpled upon the term "binary search" when I read through the different ways of finding the index of an element in a list.
I decided to give it a try myself without looking at any resources, seeing if I could implement it since the concept of it sounds
pretty simple.

Iterating over a list until the item is found is O(n), because in the worst case the element we want may be the last element
in the list, so it is possible that we have to iterate over all n-elements.

Binary search makes this on average O(log n), in return it only works if the list is sorted in ascending order.

It works by taking the element in the middle of the list and checking whether this element is the element we are looking for,
if it is bigger than the element we are looking for, we repeat the algorithm on the left half of the list, if it is smaller
we repeat it on the right side. We keep doing so until either the middle element is the element we are looking for, or
there is no elements left.

To implement this, we set 2 variables "low" and "high" (or l and h) and keep "shifting" them to the new values in question.

I used recursion to implement this, because to me it just feels more suitable for a "divide and conquer" problem. It can of course
also be done iteratively, and is arguably a tiny little bit faster because of the recursive callstack.
"""

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20]

# This was my initial attempt, which worked for most cases. I also began to realize that building new
# lists from the left and right half was pretty stupid, because building a list is also O(n) as all the elements need to be copied,
# so I increased the time complexity to O(log n^3) (because I built 2 new lists each iterations, each being O(n))
def binary_search_1(arr, value, indexes=None) -> int | None:
    size = len(arr)
    middle = size // 2

    if indexes is None:
        indexes = (0, size - 1)

    left, right = arr[:middle], arr[middle:]
    try:
        if left[-1] == value:
            return indexes[0]
    except IndexError:
        return -1

    if left[-1] < value:
        return binary_search_1(right, value, (indexes[0] + middle, indexes[1]))
    else:
        return binary_search_1(left, value, (indexes[0], indexes[1] - (size - middle)))


# I noticed that there has to be a faster way to solve this, and realized that there is no reason to keep building new lists, all I have
# to do is keep "shifting" the lower and higher point of "slice of interest". List lookup is constant, O(1), so there is no benefit to
# continually making the list smaller. It also makes me not go through the effort of updating the slice indexes of a sublist in relation to
# the grand total.
def binary_search(arr, value, low=0, high=None) -> int:

    if high is None:
        high = len(arr) - 1

    if high < low:
        return -1

    middle = (low + high) // 2

    if arr[middle] == value:
        return middle

    elif arr[middle] > value:
        return binary_search(arr, value, low, high - 1)

    else:
        return binary_search(arr, value, middle + 1, high)


# Lets look for 4
# [1, 3, 4, 6, 9, 10, 15, 24, 36, 43, 50]
#  0  1  2  3  4  5   6   7    8  9   10
#  L              ^                    H
#
# Middle value is 10, which is smaller than 4, so we take the left side
#
# [1, 3, 4, 6, 9, 10]
#  0  1  2  3  4  5
#  L     ^        H   note: middle is always low + high // 2, so here its (0 + 5) // 2 which is 2
#
# Middle value is 4, we found our value at index 2!
