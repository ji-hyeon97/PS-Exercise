import sys
from collections import deque

n, w, l = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
waiting = deque(data)
bridge = deque()
finish = []
answer = 0

while True:
    if len(finish) == n:
        break
    if len(bridge) == w:
        temp = bridge.popleft()
        if temp != 0:
            finish.append(temp)
        if len(waiting) != 0:
            if sum(bridge) + waiting[0] > l:
                bridge.append(0)
            else:
                tmp = waiting.popleft()
                bridge.append(tmp)
        else:
            bridge.append(0)
    else:
        if len(waiting) != 0:
            if sum(bridge) + waiting[0] > l:
                bridge.append(0)
            else:
                tmp = waiting.popleft()
                bridge.append(tmp)
        else:
            bridge.append(0)
    answer += 1

print(answer)