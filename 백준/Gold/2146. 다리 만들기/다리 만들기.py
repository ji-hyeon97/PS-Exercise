import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

queue = deque()
check = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ridge = []


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if check[nx][ny] == 0 and graph[nx][ny] == 1:
                check[nx][ny] = 1
                graph[nx][ny] = land
                queue.append((nx, ny))


land = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and check[i][j] == 0:
            queue.append((i, j))
            check[i][j] = 1
            graph[i][j] = land
            bfs()
            land += 1

answer = int(1e9)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            continue
        for a in range(n):
            for b in range(n):
                if graph[a][b] == 0:
                    continue
                if graph[i][j] != graph[a][b]:
                    answer = min(answer, abs(a - i) + abs(b - j))

print(answer-1)