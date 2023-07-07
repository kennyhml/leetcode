"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

EXPLANATION:

The real challenge was solving this in O(n) time and constant space O(1).

To do that, we find the center of the linked list using tortoise and hare algorithm,
then reverse the first half up until the center and compare it against the second half.

For performance improvements, we can reverse as we use tortoise and hare so we dont need to
traverse the list twice. 
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findCenterAndReverse(self, head):
        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next

        if fast:
            slow = slow.next

        return prev, slow

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first_half_end, second_half_start = self.findCenterAndReverse(head)

        while first_half_end and second_half_start:
            if first_half_end.val != second_half_start.val:
                return False

            first_half_end = first_half_end.next
            second_half_start = second_half_start.next

        return True