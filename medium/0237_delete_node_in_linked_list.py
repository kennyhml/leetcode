"""
There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.


EXPLANATION:

This problem seems super confusing at first because deleting a node seems impossible without access to its previous
node, as we are unable to change the next pointer. However if we read the description closely it actually doesnt ask
us to delete the node from memory, it tells us to just replace the value.

4 > 5 > 1 > 9           4 > 1 > 1 > 9            4 > 1  1 > 9
    ↑             ->        ↑   ↑          ->        ↪ →→→→ ↑
 to delete              copy next node              update pointer

So the solution is just simple:
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(node: ListNode):
    node.val = node.next.val
    node.next = node.next.next


    # in a real environment, we should probably do the following
    # because otherwise we have a useless unreachable node in memory
    node.val = node.next.val
    tmp = node.next.next
    node.next.next = None
    node.next = tmp