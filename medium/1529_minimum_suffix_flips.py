"""
You are given a 0-indexed binary string target of length n. 
You have another binary string s of length n that is initially set to all zeros. 
You want to make s equal to target.

In one operation, you can pick an index i where 0 <= i < n and flip all bits in 
the inclusive range [i, n - 1]. Flip means changing '0' to '1' and '1' to '0'.

Return the minimum number of operations needed to make s equal to target.

EXPLANATION:

So this is a really stupid question and im not really sure how youre meant to catch onto this without
knowing the concept behind it. Essentially the minimum number of flips we have to do is represente by
the flips in the target, if our target is 10111 we imagine it as 010111 which has exactly 3 state flips.

With that knowledge we just have to count the state flips in our target and then return that.

The reason this implementation works is based on the observation that we only need to perform a flip operation 
when encountering a transition from '0' to '1' or from '1' to '0'
"""

def minFlips(target: str) -> int:
    flips, prev = 0, "0"
    for c in target: 
        if prev != c: 
            flips += 1
        prev = c
    return flips 