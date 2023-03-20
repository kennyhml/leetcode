"""Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [1,3,2]
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: Optional[TreeNode], values=None) -> list[int]:
    if root is None:
        return []

    if values is None:
        values = []

    inorderTraversal(root.left, values)
    values.append(root.val)
    inorderTraversal(root.right, values)

    return values