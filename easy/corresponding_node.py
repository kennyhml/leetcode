"""
Given two binary trees original and cloned and given a reference to a node target in the original tree.
The cloned tree is a copy of the original tree.
Return a reference to the same node in the cloned tree.
Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

    if cloned is None:
        return

    if cloned.val == target.val:
        return cloned

    return getTargetCopy(original, cloned.left, target) or getTargetCopy(
        original, cloned.right, target
    )
