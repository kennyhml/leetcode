"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such 
that every key of the original BST is changed to the original key plus the sum of 
all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bstToGst(root: TreeNode) -> TreeNode:
    curr_sum = 0

    def dfs(node):
        nonlocal curr_sum
        if node is None:
            return

        dfs(node.right)
        curr_sum += node.val
        node.val = curr_sum
        dfs(node.left)

    dfs(root)
    return root
