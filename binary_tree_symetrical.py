"""Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center)."""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symetric(root: Optional[TreeNode]) -> bool:

    left_side_head = root.left
    right_side_head = root.right

    def is_same_node(left_side, right_side) -> bool:
        if left_side is None and right_side is None:
            return True

        if not all((left_side, right_side)) or left_side.val != right_side.val:
            return False

        return is_same_node(left_side.left, right_side.right) and is_same_node(
            left_side.right, right_side.left
        )

    return is_same_node(left_side_head, right_side_head)
