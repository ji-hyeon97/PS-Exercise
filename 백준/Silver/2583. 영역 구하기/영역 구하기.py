import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split())
queue = deque()
graph = [[0 for _ in range(n)] for _ in range(m)]
check = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    a, b, c, d = map(int, sys.stdin.readline().split())
    for i in range(a, c):
        for j in range(b, d):
            graph[j][i] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    global width
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == 1:
                continue
            if check[nx][ny] == 1:
                continue
            if check[nx][ny] == 0 and graph[nx][ny] == 0:
                queue.append((nx, ny))
                check[nx][ny] = 1
                width += 1


count = 0
width = 0
data = []
for i in range(m):
    for j in range(n):
        if check[i][j] == 0 and graph[i][j] == 0:
            queue.append((i, j))
            check[i][j] = 1
            width = 1
            bfs()
            data.append(width)
            width = 0
            count += 1
print(count)
data.sort()
for i in data:
    print(i, end=" ")