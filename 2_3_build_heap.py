# python3
# Task is to convert a given array of integers into heap.
# Example:
# 5
# 5 4 3 2 1
# Output:
# 3
# 1 4
# 0 1
# 1 3
import sys
from math import *

from datetime import datetime
import threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []
        self.heapList = [0]
        self.currentSize = 0

    def read_data(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def write_response(self):
        #print(self._data)
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self._swaps.append((i-1, mc-1))
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def generate_swaps(self):
        i = len(self._data) // 2
        self.currentSize = len(self._data)
        self.heapList = [0] + self._data[:]
        #print(self.heapList)
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def solve(self):
        #tstart = datetime.now()
        self.read_data()
        self.generate_swaps()
        self.write_response()
        #tend = datetime.now()
        #print(tend - tstart)

def main():
    heap_builder = HeapBuilder()
    heap_builder.solve()

threading.Thread(target=main).start()