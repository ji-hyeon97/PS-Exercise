import sys
from collections import deque

queue = deque()
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    if data[0] == 1:
        queue.appendleft(data[1])
    if data[0] == 2:
        queue.append(data[1])
    if data[0] == 3:
        if len(queue) == 0:
            print(-1)
        else:
            temp = queue.popleft()
            print(temp)
    if data[0] == 4:
        if len(queue) == 0:
            print(-1)
        else:
            temp = queue.pop()
            print(temp)
    if data[0] == 5:
        print(len(queue))
    if data[0] == 6:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if data[0] == 7:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    if data[0] == 8:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])