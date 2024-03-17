import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))

check = [[0 for _ in range(m)] for _ in range(n)]

count = 0
queue = deque()
queue.append((0, 0, graph[0][0], 0))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = int(1e9)


def bfs():
    global answer
    while queue:
        x, y, shape, cnt = queue.popleft()
        if x == n - 1 and y == m - 1:
            answer = min(answer, cnt)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if check[nx][ny] == 0 and graph[nx][ny] != shape:
                check[nx][ny] = 1
                queue.append((nx, ny, graph[nx][ny], cnt + 1))


bfs()
if answer == int(1e9):
    print(-1)
else:
    print(answer)