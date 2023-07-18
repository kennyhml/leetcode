"""
There are several cards arranged in a row, and each card has an associated number of points. 
The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

EXPLANATION:

The trick is to figure out that its a sliding window problem, if we can take k cards away from either end or start
then we know that we will have a n - k window of remaining values at the end, where n is the length of the array.

So all we need to do is compute the total points the array holds and then check all possible sliding window positions,
then subtract the sum of that window from our total.
"""


def maxScore(cardPoints: list[int], k: int) -> int:
    total = sum(cardPoints)
    n = len(cardPoints)

    # set window and initial best sum we can achieve, notice
    # how we go until size where size is n - k meaning that
    # this essentially simulates taking all right cards
    size = n - k 
    window_sum = sum(cardPoints[:size])
    res = total - window_sum 

    for i in range(size, n):
        # add the sum of the new point and remove old one
        window_sum += cardPoints[i] - cardPoints[i - size]
        res = max(res, total - window_sum)

    return res