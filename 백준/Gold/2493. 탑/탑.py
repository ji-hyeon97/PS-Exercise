import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

top = deque()
answer = deque()

for i in range(len(data)):
    if i == 0:
        answer.append(0)
        top.append((data[i], i + 1))
        continue
    while top:
        if data[i] > top[-1][0]:
            top.pop()
        else:
            answer.append(top[-1][1])
            break
    if len(top) == 0:
        answer.append(0)
    top.append((data[i], i + 1))
print(" ".join(map(str, answer)))