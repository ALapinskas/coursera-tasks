#Uses python3

import sys, threading
from collections import deque
from datetime import datetime
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return -1

# if __name__ == '__main__':
def main():
    #tstart = datetime.now()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = {i + 1: set() for i in range(n)}
    # print(adj)
    for (a, b) in edges:
        if a not in adj.keys():
            adj[a] = set(b)
        else:
            adj[a].add(b)
        if b not in adj.keys():
            adj[b] = set(a)
        else:
            adj[b].add(a)
    # path to check from s to t
    # print(adj)
    s, t = data[2 * m], data[2 * m + 1]
    print(len(shortest_path(adj, s, t)) - 1)
    #tend = datetime.now()
    #print(tend - tstart)

threading.Thread(target=main).start()
