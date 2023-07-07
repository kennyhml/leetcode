"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

EXPLANATION:


The main problem is that we have to go backwards from the end, but we obviously have no idea how long
the linked list is. We could walk it completely and then walk backwards until we hit the nth node from
the end, but then in the worst case we would end up traversing the linked list entirely twice.

While it is more memory expensive, I decided to opt for a solution where I simply temporarly store the index
of a linked list ive visited, when I hit the end I can compute which index I need to get my nodes from to
do the operations on.
"""

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    nodes = {}
    count = 0
    curr = head

    while curr is not None:
        nodes[count] = curr
        curr = curr.next
        count += 1

    prev = nodes.get(count - n - 1)
    post = nodes.get(count - n + 1)

    if prev is None and post is None:
        return None

    if prev is None:
        return head.next

    prev.next = post
    return head

"""
Heres another very smart solution for me to keep in mind, it essentially shifts the first pointer fowards by n-offsets
and then shifts both pointers at the same time, because of the n offset the first pointer is going to hit the end at the same
time as the second pointer will hit the nth node from the end.
"""
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(head)
    dummy.next = head
    slow = dummy
    fast = dummy
    
    for _ in range(n):
        fast = fast.next

    while fast.next != None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
