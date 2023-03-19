"""
Given the head of a sorted linked list, delete all duplicates such that each element appears 
only once. Return the linked list sorted as well.
"""
from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val=0, next: ListNode = None) -> None:
        self.val = val
        self.next = next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:

    curr = head

    while curr is not None:
        next_node = curr.next
        try:
            while next_node.val == curr.val:
                next_node = next_node.next
        except AttributeError:
            curr.next = None
            return head

        curr.next = next_node
        curr = curr.next

    return head
