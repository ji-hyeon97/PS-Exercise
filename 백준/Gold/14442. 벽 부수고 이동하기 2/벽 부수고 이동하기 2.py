import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
queue = deque()
graph = []

for _ in range(n):
    data = list(map(str, sys.stdin.readline().rstrip()))
    graph.append(data)

check = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(k+1)]
check[0][0][0] = 1
queue.append((0, 0, 0))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    while queue:
        x, y, jump = queue.popleft()

        if x == n - 1 and y == m - 1:
            return check[jump][y][x]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '0' and check[jump][ny][nx] == 0:
                    check[jump][ny][nx] = check[jump][y][x] + 1
                    queue.append((nx, ny, jump))

                if graph[nx][ny] == '1':
                    if jump < k and check[jump + 1][ny][nx] == 0:
                        check[jump + 1][ny][nx] = check[jump][y][x] + 1
                        queue.append((nx, ny, jump + 1))
    return -1


print(bfs())