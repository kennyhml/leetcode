"""
You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. 
You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. 
All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.


EXPLANATION: 

Here we have to apply a method called 'backtracking', we essentially go through all ways that we could distribut the cookies
recursively, and then update the most fair distribution we found if the current distribution is better.
"""


def distributeCookies(cookies: list[int], k: int) -> int:
    min_unfairness = float('inf')
    distribution = [0] * k
    
    def backtrack(i):
        nonlocal min_unfairness, distribution
        
        print(distribution, min_unfairness)
        if i == len(cookies):
            min_unfairness = min(min_unfairness, max(distribution))
            return
        
        # Bounding condition to stop a branch if unfairness already exceeds current optimal solution
        if min_unfairness <= max(distribution):
            return
        
        for j in range(k):
            distribution[j] += cookies[i]
            backtrack(i + 1)
            distribution[j] -= cookies[i]
    
    backtrack(0)
    return min_unfairness



distributeCookies([8,15,10,20,8], 2)