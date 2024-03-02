import sys
from collections import deque
import copy

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

safe = 0


def bfs():
    global safe
    virus = deque()
    test = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if test[i][j] == 2:
                virus.append((i, j))

    while virus:
        x, y = virus.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if test[nx][ny] == 1:
                continue
            if test[nx][ny] == 0:
                test[nx][ny] = 2
                virus.append((nx, ny))

    temp = 0
    for i in range(n):
        for j in range(m):
            if test[i][j] == 0:
                temp += 1
    safe = max(safe, temp)


def makeWall(start, count):
    if count == 3:
        bfs()
        return
    for i in range(start, n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(i, count + 1)
                graph[i][j] = 0


makeWall(0, 0)
print(safe)