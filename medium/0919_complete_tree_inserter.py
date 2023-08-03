"""
A complete binary tree is a binary tree in which every level, except 
possibly the last, is completely filled, and all nodes are as far left 
as possible.

Design an algorithm to insert a new node to a complete binary tree keeping 
it complete after the insertion.

Implement the CBTInserter class:

CBTInserter(TreeNode root) Initializes the data structure with the root of 
the complete binary tree.
int insert(int v) Inserts a TreeNode into the tree with value Node.val == val 
so that the tree remains complete, and returns the value of the parent of the inserted TreeNode.
TreeNode get_root() Returns the root node of the tree.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.level = []
        self.root = root

    def insert(self, val: int) -> int:
        if self.root is None:
            self.root = TreeNode(val)
            return None

        if not self.level:
            self.level = [self.root]

        next_level = []

        for node in self.level:
            if node.left is None:
                node.left = TreeNode(val)
                return node.val

            if node.right is None:
                node.right = TreeNode(val)
                return node.val

            next_level.extend((node.left, node.right))
        
        self.level = next_level
        return self.insert(val)

    def get_root(self) -> Optional[TreeNode]:
        return self.root