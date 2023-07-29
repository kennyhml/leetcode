"""
You are given the root of a binary tree where each node has a value 0 or 1. 

Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

EXPLANATION:

Use bit shift to make space for the next nodes bit, converting the number to base 10 at the same time.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def build_nums(node, num):
            if node is None:
                return 0

            num = (num << 1 ) + node.val
            if not node.left and not node.right:
                return num

            return build_nums(node.left, num) + build_nums(node.right, num)

        return build_nums(root, 0) 