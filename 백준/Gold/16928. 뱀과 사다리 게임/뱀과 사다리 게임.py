import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
check = [0 for _ in range(101)]
ladder = {}
snake = {}
queue = deque()

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    ladder[a] = b

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    snake[a] = b

queue.append((1, 0))
check[1] = 1
answer = int(1e9)


def bfs():
    global answer
    while queue:
        x, cnt = queue.popleft()
        if x == 100:
            answer = min(answer, cnt)
        for i in range(1, 7):
            nx = x + i
            if nx < 0 or nx > 100:
                continue
            if check[nx] == 1:
                continue
            if nx in ladder:
                check[nx] = 1
                queue.append((ladder[nx], cnt + 1))
                check[ladder[nx]] = 1
                continue
            if nx in snake:
                check[nx] = 1
                queue.append((snake[nx], cnt + 1))
                check[snake[nx]] = 1
                continue
            queue.append((nx, cnt + 1))
            check[nx] = 1


bfs()
print(answer)