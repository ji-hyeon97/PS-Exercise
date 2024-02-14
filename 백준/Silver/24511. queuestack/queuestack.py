import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

datastructure = list(map(int, sys.stdin.readline().split()))
data = []
queue = deque()

element = list(map(int, sys.stdin.readline().split()))
for i in range(len(element) - 1, -1, -1):
    if datastructure[i] == 1:
        continue
    queue.append(element[i])

t = int(sys.stdin.readline().rstrip())
value = list(map(int, sys.stdin.readline().split()))

index = 0
for i in value:
    queue.append(i)
    temp = queue.popleft()
    print(temp, end=" ")