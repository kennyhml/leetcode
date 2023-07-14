r"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the 
stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

EXPLANATION:

It makes more sense when we imagine our input as a graph, for example [7, 1, 5, 3, 6, 4] would be 

\
 \
  \            /\
   \      /\  /  \
    \    /  \/
     \  /
      \/
7     1   5 3 6  4


We notice that we only have to care about sections where our profit is rising, in other words when we bought
the stock for 1, it rises until 5 and then drops at 3, so we have to sell it before it drops.
Then we buy it again at 3 and sell it at 6. Total profit is 7
"""

def maxProfit(prices: list[int]) -> int:
    profit, bought, n = 0, prices[0], len(prices)

    for i in range(1, n):
        if prices[i] < bought:
            bought = prices[i]
        elif (j := i + 1) == n or prices[j] < prices[i]:
            profit += prices[i] - bought
            bought = prices[min(j, n - 1)]
    return profit