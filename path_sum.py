"""
Given the root of a binary tree and an integer targetSum, return true if the
tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    
    def walk(node: Optional[TreeNode], curr_sum: int ):
        if node is None:
            return False

        curr_sum += node.val
        if node.left is None and node.right is None:
            return curr_sum == targetSum

        return walk(node.left, curr_sum) or walk(node.right, curr_sum)

    return walk(root, 0)