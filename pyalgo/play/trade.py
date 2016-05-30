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


def dyn_trader(prices, k):
    n = len(prices)
    m = np.zeros((n, n))
    states = {}
    for k in range(n-1, 0, -1):
        for i in range(0, k):
            j = k - 1 - i
            m[i, j] = k
            # i+1, j
            n, first_buy, last_sell = states[(i+1, j)]
            if n < k:

            else:
                if p[i] < p[first_buy]:
                    m[i, j] = m[i+1, j] + p[first_buy] - p[i]
                    first_buy = i
                    
            # i, j+1
            print(i, j)
    print(m)


if __name__ == '__main__':
    prices = [7, 9, 10, 3]
    k = 4
    dyn_trader(prices, k)