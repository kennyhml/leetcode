"""
Given the root of a binary tree and two integers val and depth, add a row of 
nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, 
create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node 
with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

EXPLANATION:

Pretty simple, using BFS just because I think its more suitable for level based stuff.
Simply keep track of our current depth, once we are at the target depth we essentially just insert a new node
for each node at that depth.

Only edgecases to handle are root being None or depth being 1 since we need to create / replace root.
"""

from typing import Optional
class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def addOneRow(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    if not root:
        return TreeNode(val)

    if depth == 1:
        new_root = TreeNode(val)
        new_root.left = root
        return new_root
        
    current_depth = 0
    level = [root]

    while level:
        current_depth += 1
        next_level = []

        for node in level:
            if current_depth == depth - 1:
                for node in level:
                    node.left = TreeNode(val, node.left)
                    node.right = TreeNode(val, None, node.right)
                break

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        level = next_level

    return root