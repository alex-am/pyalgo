"""
test suite for data structures
"""

import unittest

from ..data.heap import Heap
from ..data.heap import HeapError
from ..data.heap import KV

class TestHeap(unittest.TestCase):
    def test_heap(self):
        h = Heap()
        h.push(1,24)
        h.push(2,2)
        h.push(4,2)
        h.push(-4,2)
        h.push(9,2)
        h.push(-3,2)
        h.push(1,2)
        h.push(7,2)
        self.assertEqual(h.pop().key, -4)
        self.assertEqual(h.pop().key, -3)
        self.assertEqual(h.pop().key, 1)
        self.assertEqual(h.pop().key, 1)
        self.assertEqual(h.pop().key, 2)
        self.assertEqual(h.pop().key, 4)
        self.assertEqual(h.pop().key, 7)
        self.assertEqual(h.pop().key, 9)

    def test_heapify(self):
        data = [KV(1,24), KV(2,2), KV(4,2), KV(-4,2), KV(9,2), KV(-3,2), KV(1,2), KV(7,2)]
        h = Heap(data)
        self.assertEqual(h.pop().key, -4)
        self.assertEqual(h.pop().key, -3)
        self.assertEqual(h.pop().key, 1)
        self.assertEqual(h.pop().key, 1)
        self.assertEqual(h.pop().key, 2)
        self.assertEqual(h.pop().key, 4)
        self.assertEqual(h.pop().key, 7)
        self.assertEqual(h.pop().key, 9)

if __name__ == '__main__':
    unittest.main()