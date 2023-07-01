"""
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id


The difficulty here was not exceeding the time limits for the get method. It could still be faster but im happy with how
it does for now. It passes :)
"""

class SnapshotArray:

    def __init__(self, length: int):
        self._arr = [{0: 0} for _ in range(length)]
        self._calls = 0

    def set(self, index: int, val: int) -> None:
        self._arr[index][self._calls] = val

    def snap(self) -> int:
        self._calls += 1
        return self._calls -1
        
    def get(self, index: int, snap_id: int) -> int:
        d = self._arr[index]
        val = d.get(snap_id)
        if val is not None:
            return val

        for i, k in enumerate(d):
            if k > snap_id:
                return d[tuple(d)[i - 1]]
        return d[tuple(d)[i]]