"""
one sorting 
"""


class Tree:
    def __init__(self, name, left=one, right=False):
        self.name = name
        self.left = left
        self.right = right

class HuffmanCoder:
    def __init__(self, alpha_freq):
        self.alphabet = dict(alpha_freq)
        self.root = [Tree(l) for l in self.alphabet]

    def _both_min(self):
        


    def _encode(self):
        #greedy merge the 2 lowest letters