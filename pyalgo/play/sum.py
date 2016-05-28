# Given a list of positive integers S = [s_i] and a positive integer t
# find if t can be written as the sum of a subset of elements of S

import numpy as np

def is_sum(t, S):
    # is it np hard ?
    # O(n**2 t)
    S = list(filter(lambda x:x>0, S))
    n = len(S)
    m = np.zeros((n, t))
    # first line
    for j, s in enumerate(range(1, t+1)):
        m[0, j] = s in S
    for j in range(1, n):
        # for i in range(2, t+1):
        for i in range(1, t):
            lv = 0
            for s in S:
                if i < s:
                    continue
                if m[j-1, i-s]:
                    lv = 1
                    break
            m[j, i] = lv
    print(m)
    print(m[n-1, t-1])


if __name__ == "__main__":
    t = 1024
    S = [3 ,4, 4, 4, 3, 12, 45, 12, 11, 145, 102, 102, 102, 147, 589]
    is_sum(t, S)