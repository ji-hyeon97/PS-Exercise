import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque()
answer = int(1e9)
check = [0 for _ in range(100001)]

queue.append(n)
check[n] = 0
temp = [0 for _ in range(100001)]

while queue:
    node = queue.popleft()
    if node == k:
        answer = min(answer, check[node])
    dx = [node - 1, node + 1, node * 2]
    for nx in dx:
        if nx < 0 or nx >= 100001:
            continue
        if check[nx] != 0:
            if check[nx] > check[node] + 1:
                queue.append(nx)
                check[nx] = check[node] + 1
                temp[nx] = node
                continue

        if check[nx] == 0:
            queue.append(nx)
            check[nx] = check[node] + 1
            temp[nx] = node

print(answer)

result = [k]
for _ in range(answer):
    result.append(temp[result[-1]])
print(*result[::-1], sep=' ')