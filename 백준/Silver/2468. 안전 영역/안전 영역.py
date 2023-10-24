import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
graph = []
top = 0
for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    top = max(max(data), top)
    graph.append(data)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0
cnt = 0
while True:
    temp = 0
    if cnt == top:
        break
    if cnt != 0:
        for i in range(n):
            for j in range(n):
                graph[i][j] = graph[i][j] - 1


    def bfs():
        global temp
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if graph[nx][ny] <= 0:
                    continue
                if check[nx][ny] == 1:
                    continue
                if check[nx][ny] == 0 and graph[nx][ny] > 0:
                    check[nx][ny] = 1
                    queue.append((nx, ny))


    queue = deque()
    check = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0 and check[i][j] == 0:
                temp += 1
                queue.append((i, j))
                bfs()
    cnt += 1
    answer = max(answer, temp)
print(answer)