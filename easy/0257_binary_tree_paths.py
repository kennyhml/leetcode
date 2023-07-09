"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.


EXPLANATION:

Recursively traverse the tree while keeping track of the current path.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(root: Optional[TreeNode]) -> list[str]:
    paths = []

    def dfs(node, path):
        if node is None:
            return

        path += f"->{node.val}" if path else str(node.val)

        if not node.left and not node.right:
            paths.append(path)
        else:
            dfs(node.left, path)
            dfs(node.right, path)

    dfs(root, "")
    return paths
