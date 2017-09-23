# Uses python3
# In this program need to check if the is a path between two vertices or not,
# Input the first line contains the n and m - the number of vertices and n number  of edges,
# the last line - two vertices u and v to check the path between them exists
# Input:
# 4 4
# 1 2
# 3 2
# 4 3
# 1 4
# 1 4
# Output:
# 1
# Explanation: there is two paths between 1 and 4: 1-4, and 1-2-3-4
import sys


class Graph:
    def __init__(self):
        # number of Vertices n, and number of Edges m
        self.n, self.m = sys.stdin.readline().split()
        # paths input
        self.paths = []
        # generated adjacency list from paths
        self.adjacency_list = {}
        # last path to check existence
        self.path_to_check = []
        # array of found paths - maybe its not the best implementation, but it works
        self.find_paths = []

    def process_input(self):
        length = int(self.m) + 1
        for line in range(length):
            x, y = sys.stdin.readline().split()
            if line != length - 1:
                # Create array of paths
                self.paths.append([x, y])
            else:
                # Path to check(the last one)
                self.path_to_check = [x, y]
        # build adjacency list from paths
        self.build_list()

    def build_list(self):
        # make reverse copy of list to work on
        paths_copy = self.paths
        paths_copy.reverse()
        while paths_copy:
            graph = paths_copy.pop()
            key = graph[0]
            value = graph[1]
            if key in self.adjacency_list:
                self.adjacency_list[key] = self.adjacency_list[key] + [value]
            else:
                self.adjacency_list[key] = [value]
            if value in self.adjacency_list:
                self.adjacency_list[value] = self.adjacency_list[value] + [key]
            else:
                self.adjacency_list[value] = [key]

    def check_the_path(self):
        x = self.path_to_check[0]
        y = self.path_to_check[1]
        # Find the way from x to y
        self.find_path(x, y)
        if self.find_paths:
            print('1')
        else:
            print('0')

    def explore(self, v):
        self.adjacency_list[v].append('Visited')
        print(self.adjacency_list[v])
        for item in self.adjacency_list[v]:
            if item is not 'Visited' and self.adjacency_list[item][-1] is not 'Visited':
                self.explore(item)
                print('Exploring list: ' + str(item))

    # Modification of explore function - return True if the path from v to z exist
    def find_path(self, v, z):
        if z in v:
            self.find_paths.append('1')
        else:
            if v not in self.adjacency_list:
                self.adjacency_list[v] = ['Visited']
            else:
                self.adjacency_list[v].append('Visited')
            for item in self.adjacency_list[v]:
                if item is not 'Visited' and self.adjacency_list[item][-1] is not 'Visited':
                    self.find_path(item, z)

    def print_output(self):
        print('print number of Vertices: ' + str(self.n))
        print('print number of Edges: ' + str(self.m))
        print('array of paths: ' + str(self.paths))
        print('path to check: ' + str(self.path_to_check))
        print('adjacency_list' + str(self.adjacency_list))


if __name__ == '__main__':
    data = Graph()
    data.process_input()
    data.check_the_path()
    #data.print_output()
