# Uses python3
# For this problem, need to compute connected components,
# Example:
# 4 2
# 1 2
# 3 2
# Output:
# 2
# Explanation:
#   1   3
#    \ /
#     2    4
#
import sys


class Graph:
    def __init__(self):
        # number of Vertices n, and number of Edges m
        self.n, self.m = sys.stdin.readline().split()
        self.paths = []
        self.adjacency_list = {}
        self.components = 0

    def process_input(self):
        length = int(self.m)
        for line in range(length):
            x, y = sys.stdin.readline().split()
            # Create array of paths
            self.paths.append([x, y])
        self.build_list()

    def build_list(self):
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
        # check if number of vertices is less then n
        if int(self.n) > len(self.adjacency_list):
            empty_cells = int(self.n) - len(self.adjacency_list) + 1
            for item in range(1, empty_cells):
                cell = self.generate_empty_cells(item)
                self.adjacency_list[cell] = None

    def generate_empty_cells(self, item):
        # Find empty item for list
        if item in self.adjacency_list.keys():
            while item in self.adjacency_list.keys():
                item *= 5
        return item

    def explore(self, v):
        self.adjacency_list[v].append('Visited')
        for item in self.adjacency_list[v]:
            if item is not 'Visited':
                if self.adjacency_list[item] and self.adjacency_list[item][-1] is not 'Visited':
                    self.explore(item)
                    # print('Exploring list: ' + str(item))

    def compute_components(self):
        for key, value in self.adjacency_list.items():
            if self.adjacency_list[key]:
                if self.adjacency_list[key][-1] is not 'Visited':
                    self.explore(key)
                    self.components += 1
            else:
                # if list is bot connected
                self.components += 1
        print(self.components)

    def print_output(self):
        print('print number of Vertices: ' + str(self.n))
        print('print number of Edges: ' + str(self.m))
        print('array of paths: ' + str(self.paths))
        print('adjacency_list' + str(self.adjacency_list))


if __name__ == '__main__':
    data = Graph()
    data.process_input()
    #data.print_output()
    data.compute_components()
