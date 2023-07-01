"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


EXPLANATION:
    The given input lists represent the numbers in reverse order.
    l1: 2 -> 4 -> 3 represents the number 342
    l2: 5 -> 6 -> 4 represents the number 465

    To find the sum, we add the corresponding digits from both lists, considering any carry-over.

    Adding the digits from right to left:
    - 2 + 5 = 7, with no carry-over
    - 4 + 6 = 10, with a carry-over of 1 (which is added to the next digit)
    - 3 + 4 + 1 (carry-over) = 8

    Therefore, the sum of 342 and 465 is 807, represented as a linked list: 7 -> 0 -> 8.

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = None
    carry = 0

    while l1 or l2:
        step = carry
        step += l1.val if l1 else 0
        step += l2.val if l2 else 0

        carry, val = divmod(step, 10)
        if head is None:
            curr = head = ListNode(val)
        else:
            curr.next = ListNode(val)
            curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry:
        curr.next = ListNode(carry)

    return head