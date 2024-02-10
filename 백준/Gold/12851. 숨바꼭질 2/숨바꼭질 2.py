import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque()
answer = int(1e9)
check = [0 for _ in range(200_010)]
method = 0
queue.append((n, 0))
check[n] = 0

while queue:
    node, cnt = queue.popleft()
    if node == k:
        if answer > check[node]:
            method = 1
            answer = min(answer, check[node])
            continue
        if answer == check[node]:
            method += 1
    dx = [node - 1, node + 1, node * 2]
    for nx in dx:
        if nx < 0 or nx > 200_009:
            continue
        if check[nx] != 0:
            if check[nx] > check[node] + 1:
                queue.append((nx, cnt + 1))
                check[nx] = check[node] + 1
                continue
            if check[nx] == cnt + 1:
                queue.append((nx, cnt + 1))

        if check[nx] == 0:
            queue.append((nx, cnt + 1))
            check[nx] = check[node] + 1

print(answer)
print(method)