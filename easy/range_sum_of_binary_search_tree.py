"""
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:

    if root is None:
        return 0

    if root.val < low:
        return 0 + rangeSumBST(root.right, low, high)

    elif root.val > high:
        return 0 + rangeSumBST(root.left, low, high)

    return (
        root.val
        + rangeSumBST(root.left, low, high)
        + rangeSumBST(root.right, low, high)
    )
