"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.


EXPLANATION:

Pretty easy, perform a bfs search on the binary tree and get the sum of each level.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxLevelSum(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    current_level = best_level = 1
    best_sum = root.val
    level = [root]

    while level:
        level_sum = 0
        next_level = []

        for node in level:
            level_sum += node.val

            if node.left:
                next_level.append(node.left)

            if node.right:
                next_level.append(node.right)

        if level_sum > best_sum:
            best_sum = level_sum
            best_level = current_level

        level = next_level
        current_level += 1

    return best_level