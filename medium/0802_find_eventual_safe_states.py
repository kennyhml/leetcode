"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1. 
The graph is represented by a 0-indexed 2D integer array graph where graph[i] 
is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node 
if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. 
The answer should be sorted in ascending order.

EXPLANATION:

First we initialize a list with the same length as the length of our nodes list, and set
every value to 0. This list will represent the state of the node at this index, 0 means
the node has never been visited, 1 means it has been visited and 2 means its a safe node.

Then, if we check whether a node is safe, we check whether we have updated this node already
and if we have, the node is safe if the nodes value is 2.

If we havent visited the node yet, we set its value to 1 and then recursively check whether the
adjacent nodes are safe, if they are not then we know the node is visited, but not safe.

If all of the adjacent nodes are safe, the node is safe.
"""

def eventualSafeNodes(graph: list[list[int]]) -> list[int]:
    n = len(graph)
    visited = [0] * n # 0 = not visited, 1 = visited, 2 = safe

    def is_safe(node):
        if visited[node] != 0:
            return visited[node] == 2

        visited[node] = 1
        
        for neighbor in graph[node]:
            if not is_safe(neighbor):
                return False

        visited[node] = 2
        return True
    
    return [i for i in range(n) if is_safe(i)]
