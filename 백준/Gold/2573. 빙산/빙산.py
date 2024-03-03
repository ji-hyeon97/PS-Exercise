import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def melt():
    year = 1
    while True:
        temp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                aside = 0
                if graph[i][j - 1] == 0:
                    aside += 1
                if graph[i][j + 1] == 0:
                    aside += 1
                if graph[i + 1][j] == 0:
                    aside += 1
                if graph[i - 1][j] == 0:
                    aside += 1
                temp[i][j] = aside

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                graph[i][j] = max(0, graph[i][j] - temp[i][j])

        def bfs():
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if graph[nx][ny] != 0 and check[nx][ny] == 0:
                        check[nx][ny] = 1
                        queue.append((nx, ny))

        island = 0
        queue = deque()
        check = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if graph[i][j] > 0 and check[i][j] == 0:
                    queue.append((i, j))
                    check[i][j] = 1
                    bfs()
                    island += 1
        if island > 1:
            return year
        year += 1
        if island == 0:
            return 0


print(melt())