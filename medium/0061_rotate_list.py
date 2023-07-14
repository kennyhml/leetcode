"""
Given the head of a linked list, rotate the list to the right by k places.

EXPLANATION:

Lets understand how we rotate the list, given the following:

Input: head = [1,2,3,4,5], k = 2

If we shift every node by k (2) places, the list ends up looking like [4,5,1,2,3]
So as we can see, every node has been shifted by k places, i.e 1 was previously at
0 and is now at 2, when a value is at the end of the list and it gets shifted, it
has to wrap around.

However shifting every value indidually would be expensive, so its faster to look for a
pattern here, notice how when we rotate the array by k places, we are essentially just 
slicing it at length - k and putting that section in front, for the above example

length = 5, k = 2
steps = length - k - 1 = 2
I dont take the -1 in my code because I start taking the steps from the tail intead of the head

1 > 2 > 3 > 4 > 5         1 > 2 > 3 X 4 > 5          4 > 5 > 1 > 2 > 3
        ↑           ->    ↑           ↑         ->   ↑       ↑
      steps              head       new head      new head  head


So, first we need to find the length of the linked list, so that we can check the 'true'
k in case k is bigger than the length of the list meaning it wraps around.

Then we make the list cirular to establish the connection between the two slices we will have
later on and we already have the last node from counting the length
anyway.
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
    
    curr.next = head
    steps = length - k
    while steps > 0:
        curr = curr.next
        steps -= 1

    # set our new head and break the old connection to this head
    # since we made the list circular before we still have it all connected
    new_head = curr.next
    curr.next = None

    return new_head