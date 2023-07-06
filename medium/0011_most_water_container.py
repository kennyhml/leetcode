"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

EXPLANATION:


Brute force obviously works but its too slow, doesnt even pass.

The right approach is similar to two sum II, we set a pointer at the start and at the end, and then
shift the pointer on the lower height. The reason this works is that for a given height h, there cannot
be a bigger container area left because the width w will now always be smaller.
"""

def maxArea(height: list[int]) -> int:
    biggest = 0
    l, r = 0, len(height) - 1

    while l < r:
        left_height, right_height = height[l], height[r]

        if left_height > right_height:
            area = (r - l) * right_height
            r -= 1
        else:
            area = (r - l) * left_height
            l += 1

        biggest = max(area, biggest)



    return biggest



def maxArea(height: list[int]) -> int:
    """This is the bruteforce solution"""
    biggest = 0
    l = len(height) - 1

    for i in range(l):
        for j in range(i + 1, l):
            low = min(height[i], height[j])
            biggest = max(biggest, low * (j - i))

    return biggest