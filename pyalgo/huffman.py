"""
one sorting 
"""

from operator import itemgetter
import queue

class Tree:
    def __init__(self, name, freq, left=None, right=None):
        self.name = name
        self.freq = freq
        self.left = left
        self.right = right

    @staticmethod
    def merge(t1, t2):
        name = "(%s_%s)" % (t1.name, t2.name)
        freq = t1.freq + t2.freq
        return Tree(name, freq, t1, t2)

class HuffmanEncoder:
    def __init__(self, alpha_freq):
        self.root = self._encode_naive(alpha_freq)

    def _both_min(self, root):
        # O(len(root))
        g = map(lambda t: (t[0], t[1].name, t[1].freq), enumerate(root))
        i1, k1, v1 = next(g)
        i2, k2, v2 = next(g)
        if v2 < v1:
            ii, ik, iv = i1, k1, v1
            i1, k1, v1 = i2, k2, v2
            i2, k2, v2 = ii, ik, iv
        for i, k, v in g:
            if v < v1:
                i2, k2, v2 = i1, k1, v1
                i1, k1, v1 = i, k, v
                continue
            if v < v2:
                i2, k2, v2 = i, k, v
        return (i1, i2)

    def _encode_naive(self, alpha_freq):
        # greedy merge the 2 lowest letters
        # O(len(root)) -> n**2
        root = [Tree(name=k, freq=v) for k, v in alpha_freq.items()]
        while len(root) > 2:
            i1, i2 = self._both_min(root)
            # print([(r.name, r.freq) for r in root])
            # print(i1, i2)
            t1 = root[i1]
            t2 = root[i2]
            # merge
            nt = Tree.merge(t1, t2)
            del root[max(i1, i2)]
            del root[min(i1, i2)]
            root.append(nt)
        t1 = root[0]
        t2 = root[1]
        name = "(%s_%s)" % (t1.name, t2.name)
        freq = t1.freq + t2.freq
        return Tree(name, freq, t1, t2)

    def encode(self, alpha_freq):
        # sorting step could be improved
        # two queues the ordered queue and the 2 min queue

        oq = queue.Queue()
        mq = queue.Queue()
        for e in sorted(alpha_freq.items(), key=itemgetter(1)):
            oq.put(e)
        #±init
        t1 = oq.get()
        t2 = oq.get()
        mq.put(t1)
        mq.put(t2)
        curs = None
        while True:
            m1 = mq.get()
            m2 = mq.get()


            else:
                merged = merge(aux, t1)
                rem = t2
                t1 = t2
                aux.put(merged)


