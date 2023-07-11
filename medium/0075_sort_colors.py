"""
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function

EXPLANATION:

The idea here is to sort with the goal in mind, we know that the biggest number is 3 and the
smallest number is 0, so we set a left and a right pointer for 0 (red) and 2 (blue), the 1s will
be between them (white).

We then start moving our white (1) pointer over the array, if we find a 0 we swap it with our 
current red (0) pointer and move both pointers to the right.

If we find a blue (2), we switch that with the white (1) pointer as well, but instead
of incrementing both, we only decrement the blue pointer.


We know we are done sorting when the white (1) pointer is bigger than the blue (2) pointer.
"""



def sortColors(nums: list[int]) -> None:
    red, white, blue = 0, 0, len(nums) - 1

    while white <= blue:
        num = nums[white]
        if num == 0:
            nums[red], nums[white] = num, nums[red]
            red += 1
            white += 1
        elif num == 2:
            nums[blue], nums[white] = num, nums[blue]
            blue -= 1
        else:
            white += 1

    return nums
