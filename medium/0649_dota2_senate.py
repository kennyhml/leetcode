"""
In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. 
Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. 

In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, 
he can announce the victory and decide on the change in the game.

Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party 
and the Dire party. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. 
This procedure will last until the end of voting. All the senators who have lost their rights will 
be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. 
Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".


EXPLANATION:

The problem description is really bad, essentially we have a string of turns like RDDRRR where R is a senate of the radiant
faction and D is the Dire faction. The senate can then ban a senate from the other faction, or announce the win (if no one from
the other faction is left.).

This essentially just boils down to two queues where the senate is represented by their index in the string, in other words
their 'turn priority', the higher priority senate of the two queue heads is at turn, and will choose to ban the other one at
turn, resulting in that one being deleted whereas the chosen one goes back to the end of the queue.
"""

from collections import deque

def predictPartyVictory(senate: str) -> str:
    n = len(senate)
    radiant, dire = deque([]), deque([])
    
    for i in range(n):
        if senate[i] == "R":
            radiant.append(i)
        else:
            dire.append(i)

    while radiant and dire:
        n += 1
        if radiant[0] < dire[0]:
            radiant.append(n)
        else:
            dire.append(n)
        radiant.popleft()
        dire.popleft()

    return "Radiant" if radiant else "Dire"