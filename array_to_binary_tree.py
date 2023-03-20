"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree."""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to_BST(nums: list[int]) -> Optional[TreeNode]:
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    root.left = array_to_BST(nums[:mid])
    root.right = array_to_BST(nums[mid + 1 :])

    return root
