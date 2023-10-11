import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
shark = deque()
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)

dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            shark.append((i, j))

answer = 0
while shark:
    x, y = shark.popleft()
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if graph[nx][ny] != 0:
            continue

        shark.append((nx, ny))
        graph[nx][ny] = graph[x][y] + 1
        answer = max(answer, graph[nx][ny])
print(answer - 1)