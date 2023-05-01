import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for i in range(m):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)

check = [[0 for i in range(n)] for j in range(m)]
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0


def bfs():
    global answer

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if check[nx][ny] == 1:
                continue
            if graph[nx][ny] != 0:
                continue
            if graph[nx][ny] == 0 and check[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                check[nx][ny] = 1
                queue.append((nx, ny))


for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and check[i][j] == 0:
            queue.append((i, j))
            check[i][j] = 1

bfs()

answer = 0
for row in graph:
    for i in row:
        if i == 0:
            print(-1)
            exit()
        if i >= answer:
            answer = i
print(answer - 1)
