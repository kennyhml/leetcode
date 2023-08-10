"""
There are three stones in different positions on the X-axis. You are given three integers 
a, b, and c, the positions of the stones.

In one move, you pick up a stone at an endpoint (i.e., either the lowest or highest position stone), 
and move it to an unoccupied position between those endpoints. Formally, let's say the stones are 
currently at positions x, y, and z with x < y < z. You pick up the stone at either position x or 
position z, and move that stone to an integer position k, with x < k < z and k != y.

The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).

Return an integer array answer of length 2 where:

answer[0] is the minimum number of moves you can play, and
answer[1] is the maximum number of moves you can play.
"""

def numMovesStones(a: int, b: int, c: int) -> list[int]:

    x, y, z = sorted([a, b, c])
    empty = len([num for num in range(x, z + 1) if num not in (x, y, z)])
    if empty == 0:
        return [0, 0]

    if x + 1 == y or z - 1 == y or x + 2 == y or z - 2 == y:
        _min = 1
    else:
        _min = 2

    return [_min, empty]