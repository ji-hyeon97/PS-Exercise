import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
answer = int(1e9)
queue = deque()
queue.append((a, 1))

while queue:
    node, times = queue.popleft()
    if node == b:
        answer = min(answer, times)
    if node < b:
        queue.append((node * 2, times + 1))
        queue.append((node * 10 + 1, times + 1))
if answer == int(1e9):
    answer = -1
print(answer)