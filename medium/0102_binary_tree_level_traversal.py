"""
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).


EXPLANATION:

Super simple BFS problem, no idea why this is listed medium.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder( root: Optional[TreeNode]) -> list[list[int]]:
    res = []
    level = [root]

    while level and root:
        next_level, vals = [], []
    
        for node in level:
            vals.append(node.val)
            if node.left:
                next_level.append(node.left)

            if node.right:
                next_level.append(node.right)

        level = next_level
        res.append(vals)

    return res