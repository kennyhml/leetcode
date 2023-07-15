f"""
You are given an integer array target. You have an integer array initial of the 
same size as target with all elements initially zeros.

In one operation you can choose any subarray from initial and increment each value by one.

Return the minimum number of operations to form a target array from initial.

The test cases are generated so that the answer fits in a 32-bit integer.

EXPLANATION:

So the problem sounds harder than it is, we just need to understand that assuming we have an array
like [1,2,3,2,1], if we are at 2 our previous number is 1, the difference between them is 1, so we 
add the difference between them to our total operations, we continue to do this for the entire array
and get the optimal solution.


[3, 1, 5, 4, 2]      [3, 1, 5, 4, 2]      [3, 1, 5, 4, 2]       [3, 1, 5, 4, 2]     [3, 1, 5, 4, 2]
 ↑                    ↑  ↑                    ↑  ↑                     ↑  ↑                   ↑  ↑
 c                    p  c                    p  c                     p  c                   p  c
 3 - 0 = 3            1 - 3 = -2           5 - 1 = 4            4 - 5 = -1           2 - 4 = - 2
 3 operations         0 operations         4 operations         0 operations         0 operations    = Total 7 operations


The reason this approach works is that the differences between adjacent elements capture the changes 
needed to reach the target values. By summing up all the positive differences, we count the necessary 
operations to increment the subarrays.

"""

def minNumberOperations(target: list[int]) -> int:
    prev = operations = target[0]
    n = len(target)

    for i in range(1, n):
        diff = target[i] - prev
        if diff > 0:
            operations += diff

        prev = target[i]

    return operations