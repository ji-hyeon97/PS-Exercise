import sys
from collections import deque

v, e = map(int, sys.stdin.readline().split())
inDegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    inDegree[b] += 1


def topology():
    result = []
    queue = deque()

    for i in range(1, v + 1):
        if inDegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)
        for i in graph[now]:
            inDegree[i] -= 1
            if inDegree[i] == 0:
                queue.append(i)
    for i in result:
        print(i, end=" ")


topology()