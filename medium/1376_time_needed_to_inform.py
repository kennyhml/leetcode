"""
A company has n employees with a unique ID for each employee from 0 to n - 1. 
The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is 
the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed 
that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. 
He will inform his direct subordinates, and they will inform their subordinates, and so on until 
all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates 
(i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.


EXPLANATION:

Important part is to realize that this is a simple DFS problem, we simply explore all paths
and check how long each path takes, the result is the biggest one.
"""

def numOfMinutes(n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
    def dfs(i):
        if manager[i] != -1:
            informTime[i] += dfs(manager[i])
            manager[i] = -1 # indicate that this employee was visited

        return informTime[i]

    return max(dfs(i) for i in range(n))