import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
queue = deque()
answer = int(1e9)

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

check = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
queue.append((r1, c1, 0))
check[r1][c1] = 1

while queue:
    x, y, cnt = queue.popleft()
    if x == r2 and y == c2:
        answer = min(answer, cnt)
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if check[nx][ny] == 1:
            continue
        queue.append((nx, ny, cnt + 1))
        check[nx][ny] = 1
if answer == int(1e9):
    print(-1)
else:
    print(answer)