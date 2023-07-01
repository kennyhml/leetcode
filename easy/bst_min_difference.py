"""
Given the root of a Binary Search Tree (BST),
return the minimum absolute difference between the values of any two different nodes in the tree.

EXPLANATION:

Since its a binary SEARCH tree we can do an inorder traversal (left, visit, right), simply keep track
of the previous node and see whether the absolute difference of the two nodes is smaller than the current one.

"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        smallest = float("inf")
        prev = None

        def inorder(node):
            nonlocal smallest, prev
            if node is None:
                return

            inorder(node.left)
            if prev is not None:
                if (diff := abs(node.val - prev)) < smallest:
                    smallest = diff
            prev = node.val
            inorder(node.right)

        inorder(root)
        return smallest