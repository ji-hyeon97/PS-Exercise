import sys
from collections import deque
import copy

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)

time = int(1e9)
flag = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    global time, flag
    virus = deque()
    test = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if test[i][j] == 3:
                virus.append((i, j, 0))
    howLong = 0
    while virus:
        x, y, times = virus.popleft()
        howLong = max(howLong, times)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if test[nx][ny] == 3:
                continue

            if test[nx][ny] == 1:
                continue

            if test[nx][ny] == 0 or test[nx][ny] == 2:
                test[nx][ny] = 3
                virus.append((nx, ny, times + 1))
    temp = 0
    for i in range(n):
        for j in range(n):
            if test[i][j] == 0 or test[i][j] == 2:
                temp = 1
                break
        if temp == 1:
            break
    if temp == 0:
        flag = 1

    if temp == 1:
        return
    time = min(time, howLong)


def makeVirus(start, count):
    if count == m:
        bfs()
        return
    for i in range(start, n):
        for j in range(n):
            if graph[i][j] == 2:
                graph[i][j] = 3
                makeVirus(i, count + 1)
                graph[i][j] = 2


makeVirus(0, 0)

if flag == 1:
    print(time)
else:
    print(-1)