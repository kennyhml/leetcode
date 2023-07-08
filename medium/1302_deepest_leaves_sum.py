"""
Given the root of a binary tree, return the sum of values of its deepest leaves.

EXPLANATION:

For a DFS (depth first search) approach we can recursively walk the nodes while keeping
track of the deepest depth we have seen and the current depth. If we find a new deepest
depth on a node we know that for now the sum of this level is going to start with the nodes
value. 


For BFS (breadth first search) we sum up the values of the currently level while simultaneously
preparing the nodes of the next level, then repeat this process until we are out of nodes.

Time complexity:
    O(n) for both search algorithms

Space complexity:
    BFS: O(m) where m is the maximum width of the binary tree
    DFS: O(h) where h is the height of the binary tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def DFS(root: Optional[TreeNode]) -> int:
    deepest_sum = max_depth = 0

    def dfs(node, depth):
        nonlocal max_depth, deepest_sum
        if node is None:
            return

        if depth == max_depth:
            deepest_sum += node.val

        elif depth > max_depth:
            max_depth = depth
            deepest_sum = node.val

        depth += 1
        dfs(node.left, depth)
        dfs(node.right, depth)
        
    dfs(root, 0)
    return deepest_sum


def BFS(root: Optional[TreeNode]) -> int:
    level = [root]

    while level and root:
        next_level, level_sum = [], 0

        for node in level:
            level_sum += node.val

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
        
    return level_sum