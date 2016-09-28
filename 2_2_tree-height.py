# python3
# Find the height of given tree
# Example input:
# 10
# 8 8 5 6 7 3 1 6 -1 5
# Tree height: is 6


import sys, threading
#from datetime import datetime
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
            try:
                self.n = sys.stdin.readline()
                self._parents = list(map(int, sys.stdin.readline().split()))
                self._max_depth = 0
                self._depths = [0 for i in range(int(self.n))]
            except ValueError:
                pass

        def max_depth(self):
            if self._max_depth == 0:
                # foreach item count items depth, and return the biggest one
                for idx, parent in enumerate(self._parents):
                    depth = self.get_depth(idx)
                    #print('depth  ' + str(depth))
                    if int(self._max_depth) < int(depth):
                        self._max_depth = depth
            return self._max_depth

        def get_depth(self, idx):
            depth = self._depths[idx]
            if depth > 0:
                return depth
            parent = self._parents[idx]
            if parent == -1:
                depth = 1
            else:
                depth = self.get_depth(parent) + 1
            self._depths[idx] = depth
            return int(depth)


def main():
  #tstart = datetime.now()
  tree = TreeHeight()
  tree.read()
  print(tree.max_depth())
  #tend = datetime.now()
  #print(tend - tstart)

threading.Thread(target=main).start()
