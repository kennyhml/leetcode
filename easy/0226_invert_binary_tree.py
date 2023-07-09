"""
Given the root of a binary tree, invert the tree, and return its root.

EXPLANATION:

Pretty straightfoward when you think about it, if we swap the nodes left and right nodes
and repeat it for every node, the tree will end up inversed.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(node):
            if node is None:
                return

            node.left, node.right = node.right, node.left
            swap(node.left)
            swap(node.right)

        swap(root)
        return root