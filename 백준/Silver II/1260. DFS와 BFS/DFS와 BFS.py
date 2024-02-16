import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
queue = deque()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

check = [0 for _ in range(n + 1)]


def dfs(idx):
    print(idx, end=" ")
    data = sorted(graph[idx])
    for i in data:
        if check[i] == 0:
            check[i] = 1
            dfs(i)


check[v] = 1
dfs(v)
print("")

check = [0 for _ in range(n + 1)]
queue.append(v)
check[v] = 1


def bfs():
    while queue:
        idx = queue.popleft()
        print(idx, end=" ")
        data = sorted(graph[idx])
        for i in data:
            if check[i] == 0:
                check[i] = 1
                queue.append(i)


bfs()