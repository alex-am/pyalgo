# Given a list of positive integers S = [s_i] and a positive integer t
# find if t can be written as the sum of a subset of elements of S

import numpy as np

def is_sum(t, S):
    # is it np hard ?
    # O(n**2 t)
    # brute force 2**n
    S = list(filter(lambda x:x>0, S))
    n = len(S)
    m = np.zeros((n, t), dtype=np.int)
    # first line
    for s in range(0, t):
        m[0, s] = s + 1
    #we can be lucky

    for j in range(1, n):
        for i in range(1, t):
            for s in S:
                if i < s:
                    continue
                if m[j-1, i-s]:
                    m[j, i] = s
                    if i == (t-1):
                        #reached the target we are done
                        return (j, m)
                    break
    return (j, m)

def get_shortest(i, m):
    _, t = m.shape
    res = []
    while i >= 0:
        e = m[i, t-1]
        res.append(e)
        t = t - e
        if t <= 0:
            break
        i -= 1
    return res

if __name__ == "__main__":
    t = 12
    S = [3 ,4, 4, 4, 3, 12, 45]
    i, m = is_sum(t, S)
    print(i, m)
    print(get_shortest(i, m))