"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

EXPLANATION:

Similar to 'find eventual safe state' question, just that we have to make our own graph
first.

I like to imagine it the same way importing a module works in python, if a module is being loaded
we set its state to -1 and then go to load its dependencies, if while we load those we run into a 
-1 state module, theres a circular import somewhere and it doesnt work.
"""


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:

    graph = [[] for _ in range(numCourses)]
    for course, prerequisite in prerequisites:
        graph[course].append(prerequisite)

    visited = [0] * numCourses
    
    def dfs(course):
        if (state := visited[course]) != 0:
            return state == 1

        visited[course] = -1

        for neighbour in graph[course]:
            if not dfs(neighbour):
                return False

        visited[course] = 1
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False

    return True