import sys
from collections import deque

dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]

while True:
    a, b = map(int, sys.stdin.readline().split())
    queue = deque()
    if a == 0 and b == 0:
        break
    graph = []
    for _ in range(b):
        data = list(map(int, sys.stdin.readline().split()))
        graph.append(data)
    check = []
    for _ in range(b):
        data = [0 for _ in range(a)]
        check.append(data)


    def bfs():
        while queue:
            x, y = queue.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= b or ny >= a:
                    continue
                if check[nx][ny] == 0 and graph[nx][ny] == 1:
                    check[nx][ny] = 1
                    queue.append((nx, ny))


    answer = 0
    for i in range(b):
        for j in range(a):
            if check[i][j] == 0 and graph[i][j] == 1:
                check[i][j] = 1
                answer += 1
                queue.append((i, j))
                bfs()
    print(answer)