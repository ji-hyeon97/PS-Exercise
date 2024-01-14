import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
queue = deque(data)
wait = []
answer = []
index = 1

while True:
    if len(queue) == 0:
        break
    if queue[0] == index:
        temp = queue.popleft()
        answer.append(temp)
        index += 1
        continue
    if len(wait) != 0:
        if wait[-1] == index:
            temp = wait.pop()
            answer.append(temp)
            index += 1
            continue
    temp = queue.popleft()
    wait.append(temp)
if len(wait) != 0:
    tmp = sorted(wait, reverse=True)
    if tmp == wait:
        print("Nice")
    else:
        print("Sad")
else:
    print("Nice")