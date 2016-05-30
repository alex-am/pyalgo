"""
test suite for huffman algo
"""

import unittest

from ..huffman import HuffmanEncoder

class TestHuffman(unittest.TestCase):
    def test_huf(self):
        h = {'a':2.5, 'b':9, 'c':2, 'd':9, 'e':1}
        q = HuffmanEncoder(h).encode(h)
        while not q.empty():
            print(q.get(False))