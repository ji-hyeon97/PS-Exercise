import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

for _ in range(n):
    queue = deque()
    t = int(sys.stdin.readline().rstrip())
    graph = [[0 for _ in range(t)] for _ in range(t)]
    check = [[0 for _ in range(t)] for _ in range(t)]
    a, b = map(int, sys.stdin.readline().split())
    c, d = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    check[c][d] = 1
    queue.append((c, d, 1))
    answer = int(1e9)
    while queue:
        x, y, index = queue.popleft()
        if x == a and y == b:
            answer = 0
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= t or ny >= t:
                continue
            if check[nx][ny] == 1:
                continue
            if graph[nx][ny] == 1:
                answer = min(answer, index)
                break
            if graph[nx][ny] == 0 and check[nx][ny] == 0:
                check[nx][ny] = 1
                queue.append((nx, ny, index + 1))
    print(answer)