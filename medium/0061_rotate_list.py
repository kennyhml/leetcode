"""
Given the head of a linked list, rotate the list to the right by k places.

EXPLANATION:

First we need to find the length of the linked list, so that we can check the 'true'
k in case k is bigger than the length of the list meaning it wraps around.

Once thats done we can make the list circular temporarily as it will help a ton
to rotate it later, and we already have the last node from counting the length
anyway.

We then compute the amount of nodes we have to walk, since we are currently at the tail node
the new head will be at position length - k, i.e if our linked list is 10 nodes long and
k is 4, then the 6th node will be our new tail and the 7th node will be our new head
"""

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next or k == 0:
        return head

    length, curr = 1, head
    while curr.next:
        curr = curr.next
        length += 1
    
    # Take modulo k in case k > length
    k %= length
    if k == 0:
        return head

    # Make the list temporarily cirular
    curr.next = head

    steps = length - k
    while steps > 0:
        curr = curr.next
        steps -= 1

    new_head = curr.next
    curr.next = None

    return new_head