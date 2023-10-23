import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
graph = []
queue = deque()
result = []

for i in range(n):
    data = list(map(str, sys.stdin.readline().rstrip()))
    graph.append(data)
check = [[0 for _ in range(n)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
temp = 0


def bfs():
    global temp
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == '0':
                continue
            if check[nx][ny] == 1:
                continue
            if check[nx][ny] == 0 and graph[nx][ny] == '1':
                temp += 1
                queue.append((nx, ny))
                check[nx][ny] = 1
    if temp == 0:
        result.append(1)
    else:
        result.append(temp)


for i in range(n):
    for j in range(n):
        if check[i][j] == 0 and graph[i][j] == '1':
            queue.append((i, j))
            bfs()
            temp = 0
print(len(result))
result.sort()
for i in result:
    print(i)