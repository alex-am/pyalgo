""" Heap
If A is a parent node of B then the key (the value)
of node A is ordered with respect to the key of node B
binary tree implementation
"""
from collections import namedtuple
import copy

BASE_L = 2 ** 1

KV = namedtuple('kv', ('key', 'value'))

class HeapError(Exception):
    pass

class Heap:
    def __init__(self, data=None):
        # indices are all 1 based i.e. array[0]
        # is data of index 1
        if not data:
            self.array = [None for _ in range(BASE_L)]
            self.n = 0 #index of next available slot
        else:
            self.array = [copy.copy(x) for x in data]
            self.n = len(self.array)
            self._heapify()

    def parent(self, i):
        return i // 2

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def peek(self):
        if self.n:
            return self.array[0]
        raise HeapError("heap is empty")

    def _check_for_increase(self):
        l = len(self.array)
        if self.n == l:
            print("from % i" % len(self.array))
            self.array.extend([x for x in range(l)])
            print("increased to % i" % len(self.array))

    def push(self, key, value):
        # O(h)
        self._check_for_increase()
        self.n += 1
        index = self.n
        self.array[index - 1] = KV(key, value)
        while index > 1:
            if self.array[self.parent(index) - 1].key > key:
                inter = self.array[self.parent(index) - 1]
                self.array[self.parent(index) - 1] = self.array[index - 1]
                self.array[index - 1] = inter
                index = self.parent(index)
                continue
            break

    def pop(self):
        # O(h)
        if not self.n:
            raise HeapError("can t pop heap is empty")
        res = self.array[0]
        self.array[0] = self.array[self.n - 1]
        self.n -= 1
        index = 1
        while self.left(index) <= self.n:
            m_index = index
            if self.array[self.left(index)-1].key < self.array[index-1].key:
                m_index = self.left(index)
            if self.array[self.right(index)-1].key < self.array[m_index-1].key:
                m_index = self.right(index)
            if m_index == index:
                break
            inter = self.array[index-1]
            self.array[index-1] = self.array[m_index-1]
            self.array[m_index-1] = inter
            index = m_index
        return res

    def _heapify(self):
        # O(n)
        index = self.n
        while index > 1:
            if self.array[self.parent(index)-1].key > self.array[index-1].key:
                inter = self.array[self.parent(index)-1]
                self.array[self.parent(index)-1] = self.array[index-1]
                self.array[index-1] = inter
            index -= 1
