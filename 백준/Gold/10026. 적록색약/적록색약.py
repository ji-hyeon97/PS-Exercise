import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
    data = list(map(str, sys.stdin.readline().rstrip()))
    graph.append(data)

normal = deque()
abnormal = deque()
check = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs1():
    while normal:
        x, y = normal.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if check[nx][ny] == 1:
                continue
            if check[nx][ny] == 0 and graph[nx][ny] == temp:
                normal.append((nx, ny))
                check[nx][ny] = 1


result1 = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R' and check[i][j] == 0:
            normal.append((i, j))
            check[i][j] = 1
            temp = 'R'
            bfs1()
            result1 += 1
        if graph[i][j] == 'G' and check[i][j] == 0:
            normal.append((i, j))
            check[i][j] = 1
            temp = 'G'
            bfs1()
            result1 += 1
        if graph[i][j] == 'B' and check[i][j] == 0:
            normal.append((i, j))
            check[i][j] = 1
            temp = 'B'
            bfs1()
            result1 += 1
colors = ['R', 'G']
check = [[0 for _ in range(n)] for _ in range(n)]
result2 = 0


def bfs2():
    while abnormal:
        x, y = abnormal.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if check[nx][ny] == 1:
                continue
            if check[nx][ny] == 0 and graph[nx][ny] in colors:
                abnormal.append((nx, ny))
                check[nx][ny] = 1


def bfs3():
    while abnormal:
        x, y = abnormal.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if check[nx][ny] == 1:
                continue
            if check[nx][ny] == 0 and graph[nx][ny] == 'B':
                abnormal.append((nx, ny))
                check[nx][ny] = 1


for i in range(n):
    for j in range(n):
        if check[i][j] == 0 and graph[i][j] in colors:
            abnormal.append((i, j))
            result2 += 1
            check[i][j] = 1
            bfs2()
        if check[i][j] == 0 and graph[i][j] == 'B':
            abnormal.append((i, j))
            result2 += 1
            check[i][j] = 1
            bfs3()
print(result1, result2)