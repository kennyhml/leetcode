"""
Given the head of a linked list and an integer val, remove all the nodes of 
the linked list that has Node.val == val,and return the new head.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:

    dummy = ListNode(51, next=head)
    curr = dummy

    while curr is not None:
        tmp = curr.next

        while tmp and tmp.val == val:
            tmp = tmp.next
        
        curr.next = tmp
        curr = tmp

    return dummy.next