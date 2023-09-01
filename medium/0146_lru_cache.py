"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, 
add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.max = capacity
        self.map = {}

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        element = self.map.pop(key)
        self.map[key] = element
        return element
        
    def put(self, key: int, value: int) -> None:
        if not self.map.pop(key, None) and len(self.map) == self.max:
            self.map.pop(next(iter(self.map)))

        self.map[key] = value