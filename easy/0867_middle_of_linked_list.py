"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""
from typing import Optional

class ListNode:
    def __init__(self, next=None, val=None) -> None:
        self.next = next
        self.val = val

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow