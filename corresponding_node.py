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
