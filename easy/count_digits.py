"""
Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.

EXPLANATION:
------------

Copy paste of my solution post on leetcode:

Approach
'Mathematical' pre-requisites to understand the solution:

num % 10 will yield the last digit of num
num //= 10 will remove the last digit of num

First we need to create a temporary variable that will start off having the same value as our num, 
thats because we need a variable to do the 'iteration' on, and also the original variable to check 
whether the digit of our current iteration evenly divides the number.

We can then start going through the digits in our number by using the operations listed above, 
it will of course be in reverse but it doesnt matter in this case, since we are just counting even divisors.

We know that we are done when temp is exhausted, i.e it is 0. Remember that 0 has a False truthy value, 
so while temp is equivalent to while temp != 0.

Complexity
Time complexity: O(log10(num))

Space complexity: O(n) (constant)
"""

def countDigits(num: int) -> int:
    count = 0
    tmp = num

    while tmp:
        digit = tmp % 10
        if num % digit == 0:
            count += 1
        tmp //= 10
    return count