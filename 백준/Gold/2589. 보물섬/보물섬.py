import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
graph = []
for _ in range(a):
    data = list(map(str, sys.stdin.readline().rstrip()))
    graph.append(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
top = 0

def bfs(check, dist):
    global top
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= a or ny >= b:
                continue

            if graph[nx][ny] == 'W':
                continue

            if check[nx][ny] == 0 and graph[nx][ny] == 'L':
                check[nx][ny] = 1
                queue.append((nx, ny))
                dist[nx][ny] = max(dist[nx][ny],dist[x][y] + 1)
                top = max(top,dist[nx][ny])



for i in range(a):
    for j in range(b):
        check = [[0 for _ in range(b)] for _ in range(a)]
        dist = [[0 for _ in range(b)] for _ in range(a)]
        if graph[i][j] == 'L':
            queue.append((i, j))
            check[i][j] = 1
            bfs(check, dist)
print(top)