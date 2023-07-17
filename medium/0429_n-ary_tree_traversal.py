"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children 
is separated by the null value (See examples).

EXPLANATION:

Basically typical binary tree BFS, just that instead of a left and right attribute, we have
a 'children' attribute which represents a list of children this node has, so exact same approach
just a tiny change.
"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def levelOrder(root: Node) -> list[list[int]]:
    res = []
    level = [root]

    while level and root:
        next_level, vals = [], []
    
        for node in level:
            vals.append(node.val)
            for child in node.children:
                next_level.append(child)

        level = next_level
        res.append(vals)

    return res