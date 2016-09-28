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
from heapq import heappush, heappop

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []
        self._check_table = {}
        self._minel = 0
        self._iteration = 0

    def read_data(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        i = 0
        for value in self._data:
            self._check_table[i] = value
            i = i + 1

        assert n == len(self._data)

    def write_response(self):
        print(self._data)
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def generate_swaps(self):
        #Find the min element in the list, and its index
        #print('check table ' + str(self._check_table))
        self._minel = min(self._check_table.values())
        print(key)
        minel_index = self._data.index(self._minel)
        print('min el ' + str(self._minel))
        # print('original table ' + str(self._data))
        print('min el index of original table ' + str(minel_index))
        #Find parent of min element, and its index
        parentel_index = self.Parent(minel_index + 1)
        parentel = self._data[parentel_index]
        # print('parent - min ' + str(self._data[parentel_index]) + ' - ' + str(self._data[minel_index]))
        # if element is not at the top
        if self._data[parentel_index] > self._data[minel_index]:
            # print('minel ' + str(minel))
            # print('index parentel ' + str(parentel_index))
            #print('firstel ' + str(firstel))
            #Swap min element with its parent, until, min element get to top
            self._swaps.append((parentel_index, minel_index))
            self._data[parentel_index] = self._minel
            self._data[minel_index] = parentel
            # print(self._data)
            if self.Parent(self._minel) != self._data.index(self._minel):
                self.generate_swaps()
            else:
                # remove element from checking
                #print('else reach top' + str(self._check_table))

                #print(str(self._check_table))
                #check next
                if self._check_table:
                    self.generate_swaps()
        else:
            print(self._check_table)
            self._check_table.pop(self._check_table.index(self._minel))
            # check next
            if self._check_table:
                self.generate_swaps(iteration)
            else:
                return True

    def Parent(self, el):
        parent = floor((el)/2)
        if parent > 0:
            parent -= 1
        else:
            parent = 0
        #print('parent number ' + str(el) + ' with value:' + str(self._data[el-1]) + ' is ' + str(parent))
        return parent

    def solve(self):
        self.read_data()
        self.generate_swaps()
        self.write_response()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.solve()
