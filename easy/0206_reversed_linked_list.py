"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

EXPLANATION:

Pretty straightforward, we keep a pointer to the previous node and just assign the next nodes next pointer
to it. Before we can do that we have to make sure to store the old .next pointer since otherwise we will 
break the chain and lose the remaining pointers.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    curr, prev = head, None

    while curr is not None:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    return prev