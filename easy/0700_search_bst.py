"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree 
rooted with that node. If such a node does not exist, return null.
"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    def dfs(node):
        if node is None:
            return None

        if node.val == val:
            return node

        return dfs(node.right if node.val < val else node.left)

    return dfs(root)