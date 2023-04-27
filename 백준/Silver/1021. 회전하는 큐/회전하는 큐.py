import sys
from collections import deque

queue = deque()
n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

for i in range(1, n + 1):
    queue.append(i)

count = 0
for i in data:
    while True:
        if queue[0] == i:
            queue.popleft()
            break

        index = queue.index(i)

        if index <= len(queue) / 2:
            value = queue.popleft()
            queue.append(value)

        if index > len(queue) / 2:
            value = queue.pop()
            queue.appendleft(value)

        count += 1

print(count)
