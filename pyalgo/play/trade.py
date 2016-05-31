"""
In share trading, a buyer buys shares and sells on future date.
Given stock price of n days, the trader is allowed to make at most k transactions,
where new transaction can only start after previous transaction is complete,
find out maximum profit that a share trader could have made.

Input:  
Price = [12, 14, 17, 10, 14, 13, 12, 15]
    K = 3
Output:  12
Trader earns 12 as sum of 5, 4 and 3
Buy at price 12, sell at 17, buy at 10 
and sell at 14 and buy at 12 and sell
at 15
"""

import numpy as np

def single_trade(prices):
    # outputs best single trade from index n of price array
    # brute force for now but could do better
    # O(n**2)
    l = len(prices)
    s = prices[:]
    s[-1] = 0
    for i in range(l-1):
        m = max((prices[j] for j in range(i+1, l)))
        s[i] = m - s[i]
    return s

def dyn_trader(prices, K):
    N = len(prices)
    m = np.zeros((K, N))
    s = single_trade(prices)
    m[0,] = first_line(prices)
    for k in range(2, K+1):
        for n in range(1, N-2):
            m[k, n] = m[k-1, n] + s[n+1]
    print(m)


if __name__ == '__main__':
    prices = [7, 9, 10, 3]

    k = 4
    dyn_trader(prices, k)