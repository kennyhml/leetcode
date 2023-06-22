"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root: Optional[TreeNode]) -> list[int]:
    paths = []

    def walk(node: Optional[TreeNode]):
        if node is None:
            return

        walk(node.left)
        walk(node.right)
        paths.append(node.val)

    walk(root)
    return paths


