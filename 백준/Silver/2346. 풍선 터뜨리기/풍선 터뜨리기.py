import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
queue = deque()

for i in range(1, n + 1):
    queue.append((data[i - 1], i))

answer = []

while True:
    if len(queue) == 0:
        break
    a, b = queue.popleft()
    print(b,end=" ")
    if a > 0:
        for _ in range(a - 1):
            if len(queue) == 0:
                break
            c, d = queue.popleft()
            queue.append((c, d))
    else:
        for _ in range(-1 * a):
            if len(queue) == 0:
                break
            c, d = queue.pop()
            queue.appendleft((c, d))