import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()


def bfs():
    global temp
    while queue:
        start, end, cnt = queue.popleft()
        if start == end:
            temp = min(temp, cnt)
            return
        for i in graph[start]:
            if check[i] == 0:
                check[i] = 1
                queue.append((i, end, cnt + 1))


answer = []
for i in range(1, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        queue = deque()
        if i != j:
            temp = int(1e9)
            check = [0 for _ in range(n + 1)]
            queue.append((i, j, 0))
            bfs()
            tmp += temp
    answer.append((tmp, i))

answer.sort(key=lambda v: (v[0], v[1]))
print(answer[0][1])