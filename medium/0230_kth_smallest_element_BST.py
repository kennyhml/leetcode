"""
Given the root of a binary search tree, and an integer k, return the kth smallest value 
(1-indexed) of all the values of the nodes in the tree.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    vals = []

    def dfs(node):
        if node is None or len(vals) > k:
            return

        dfs(node.left)
        vals.append(node.val)
        dfs(node.right)

    dfs(root)
    return vals[k - 1]
