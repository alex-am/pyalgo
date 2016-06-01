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

def bf_left(prices):
    # pretty dire implemetation
    # O(n**3)
    # for fine grained proof e.g. https://en.wikipedia.org/wiki/Faulhaber%27s_formula
    l = len(prices)
    s = [None] * l
    for e in range(1, l):
        m = []
        for i_s in range(0, e):
            last_max = max((prices[j] for j in range(i_s+1, e+1)))
            m.append(last_max - prices[i_s])
        s[e] = max(m)
    return s

def bf_right(prices):
    # exactly like left but here
    # the bound is given by the starting point
    l = len(prices)
    s = [None] * l
    for b_s in range(0, l-1):
        m = []
        for i_s in range(b_s, l-1):
            last_max = max((prices[j] for j in range(i_s+1, l)))
            m.append(last_max - prices[i_s])
        s[b_s] = max(m)
    return s

def single_best(prices, index_start, index_end):
    # pretty horrible implementation
    # brute force could be improved
    # l = index_end - index_start + 1
    # O(l**2)
    res = []
    for s in range(index_start, index_end):
        res.append(max(prices[(s+1):(index_end+1)]) - prices[s])
    return max(res)

def bf_all(prices):
    # best for 1 trade between index i and j
    # pretty bad could be pythonified a bit
    # O(l**2 * single_best) = O(l**4) pretty bad
    S = []
    l = len(prices)
    for s in range(0, l-1):
        n_l = [None] * l
        for e in range(s+1, l):
            #bf result
            # for n_s in range(s, e):
            #     res = max(prices[(n_s+1):(e+1)]) - prices[n_s]
            #     m.append(res)
            # n_l[e] = max(m)
            n_l[e] = single_best(prices, s, e)
        S.append(n_l)
    return S


def dyn_trader(prices, K):
    # O(l**4) from init
    # O(k l**2) => work on init
    N = len(prices)
    optimal_nb_trades = 0
    optimal_pl = 0
    S = []
    single = bf_all(prices)
    S_init = single[0]
    m = max((x for x in S_init if x is not None))
    if m > optimal_pl:
        m = optimal_pl
        optimal_nb_trades = 1
    S.append(S_init)
    for k in range(1, K):
        n_S = [None] * N # best en k trades en regardant les prix up to h
        for end_trade in range(2*k+1, N):
                n_S[end_trade] = max((S[k-1][h] + single[h+1][end_trade] for h in range(2*k-1, end_trade - 1)))
        m = max((x for x in n_S if x is not None), default=None)
        if (m is not None) and (m > optimal_pl):
            optimal_pl = m
            optimal_nb_trades = k
        S.append(n_S)
    return (S, optimal_nb_trades, optimal_pl)


if __name__ == '__main__':
    prices = [7, 9, 10, 3]
    k = 4
    dyn_trader(prices, k)