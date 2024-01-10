import sys
from collections import deque

a,b = map(int,sys.stdin.readline().split())
data = []
for i in range(1,a+1):
    data.append(i)
queue = deque(data)
index = 0
while True:
    if len(queue) == 0:
        break
    index += 1
    if index == 1:
        print("<", end="")
    if index%b == 0:
        temp = queue.popleft()
        if len(queue) == 0:
            print(temp,end=">")
            continue
        print(temp,end=", ")
        continue
    tmp = queue.popleft()
    queue.append(tmp)