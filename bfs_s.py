# Uses python3
# Find the shortest path from one point to another(last line)
# Example:
# 4 4
# 1 2
# 4 1
# 2 3
# 3 1
# 2 4
# Output:
# 2
# Explanation:
# 4   3
# | / |
# |/  |
# 1---2
# The shortest path: 2-1-4

import sys
from datetime import datetime

def bfs(graph, start, end):
    # path var for store current path
    path = {start: 0}
    # visited dict, store key - visited vertices, value - path from the start
    # query - to store current queue items
    queue = [start]
    while queue:
        # take last element from the queue
        u = int(queue.pop())
        # set it to visited and add current path
        if u is int(end):
            return path[end]
        # go trough its children
        for child in graph[u]:
            # if child is not visited yet
            # print(path)
            # print(child)
            # print(queue)
            # print('-------')
            if int(child) not in path.keys() and child not in queue:
                # add it to queue
                queue.insert(0, child)
                path[int(child)] = path[u] + 1
    else:
        return -1


if __name__ == '__main__':
    # take input, and split it to the data
    #tstart = datetime.now()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # create an adjacency list
    adj = {i + 1: set() for i in range(n)}
    # print(adj)
    for (a, b) in edges:
        if a not in adj.keys():
            adj[a] = set(str(b))
        else:
            adj[a].add(str(b))
        if b not in adj.keys():
            adj[b] = set(str(a))
        else:
            adj[b].add(str(a))
    # path to check from s to t
    # print(adj)
    s, t = data[2 * m], data[2 * m + 1]
    print(bfs(adj, s, t))
    #tend = datetime.now()
    #print(tend - tstart)