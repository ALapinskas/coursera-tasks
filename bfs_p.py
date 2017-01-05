#Uses python3

import sys, threading
from collections import deque
from datetime import datetime
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def distance(graph, start, end):
    q = deque()
    path = (start,)
    q.append(path)
    visited = set([start])
    while q:
        path = q.popleft()
        last_node = path[-1]
        if last_node == end:
            return len(path) - 1
        for node in graph[last_node]:
            if node not in visited:
                visited.add(node)
                q.append(path + (node,))
    else:
        return -1


#if __name__ == '__main__':
def main():
    #tstart = datetime.now()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    #print(data)
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    edges.sort()
    #print(edges)
    adj = [[] for _ in range(n)]
    #print(adj)
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    #print(adj)
    print(distance(adj, s, t))
    #tend = datetime.now()
    #print(tend - tstart)

threading.Thread(target=main).start()
