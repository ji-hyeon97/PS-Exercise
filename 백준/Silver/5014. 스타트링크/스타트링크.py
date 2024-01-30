import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())
queue = deque()
method = int(1e9)

queue.append((s, g, 0))
check = [0 for _ in range(f + 1 + u)]
check[s] = 1

while queue:
    start, end, count = queue.popleft()
    if start == end:
        method = min(method, count)
        break
    if start < end and start + u <= f and check[start + u] == 0:
        check[start + u] = 1
        queue.append((start + u, end, count + 1))
    if start < end and start + u > f and check[start - d] == 0 and start - d >= 1:
        check[start - d] = 1
        queue.append((start - d, end, count + 1))
    if start > end and start - d >= 1 and check[start - d] == 0:
        check[start - d] = 1
        queue.append((start - d, end, count + 1))
    if start > end and start - d < 1 and check[start + u] == 0 and start + u <= f:
        check[start + u] = 1
        queue.append((start + u, end, count + 1))

if method == int(1e9):
    print("use the stairs")
else:
    print(method)