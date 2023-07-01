"""
There is a stream of n (idKey, value) pairs arriving in an arbitrary order, 
where idKey is an integer between 1 and n and value is a string. No two pairs have the same id.

Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) 
of values after each insertion. The concatenation of all the chunks should result in a list of the sorted values.

Implement the OrderedStream class:

OrderedStream(int n) Constructs the stream to take n values.
String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, 
then returns the largest possible chunk of currently inserted values that appear next in the order.
"""

from typing import Optional


class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 0
        self.slots: list[Optional[str]] = [None for _ in range(n)]
        
    def insert(self, idKey: int, value: str) -> list[str]:
        self.slots[idKey - 1] = value

        if self.ptr != idKey - 1:
            return []
            
        ret = []
        for idx, slot in enumerate(self.slots):
            if idx < self.ptr:
                continue
            if not slot:
                break
            ret.append(slot)

        self.ptr = idx
        return ret