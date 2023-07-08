"""
You are given the head of a linked list, which contains a series of integers separated by 0's.
The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose 
value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.

EXPLANATION:

Dummy head to take care of cases where no head is given and to make it easier to start the summing
since the first node is guaranteed to be 0


When we hit a 0 value node, remember that node and sum up all the nodes that come after it up until the
next 0 value node, then change the nodes value we started at to the value of the sum and set its pointer to
point to the node we stopped at.

Repeat until the node after the 0 is null.
"""

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:

    curr = dummy = ListNode(-1, next=head)

    while curr is not None:
        if curr.val != 0:
            curr = curr.next
            continue

        tmp = curr
        _sum = 0
        while curr.next.val != 0:
            curr = curr.next
            _sum += curr.val

        tmp.val = _sum
        curr = curr.next
        if curr.next is None:
            curr = tmp.next = None
        else:
            tmp.next = curr

    return dummy.next