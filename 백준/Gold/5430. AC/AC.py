import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    command = list(map(str, sys.stdin.readline().rstrip()))
    n = int(sys.stdin.readline().rstrip())
    data = sys.stdin.readline().rstrip()
    data = data.replace("[", '').replace("]", '').split(",")
    queue = deque()
    for i in data:
        if i == '':
            continue
        queue.append(i)
    flip = 0
    flag = 0
    for i in command:
        if i == 'R':
            flip += 1
        if i == 'D':
            if len(queue) == 0:
                print("error")
                flag = 1
                break
            else:
                if flip % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 1:
        continue
    if len(queue) == 0:
        print("[]")
        continue
    answer = "["
    if flip % 2 == 0:
        for i in range(len(queue)):
            answer += str(queue[i])
            if i != len(queue) - 1:
                answer += ","
        answer += "]"
    else:
        queue.reverse()
        for i in range(len(queue)):
            answer += str(queue[i])
            if i != len(queue) - 1:
                answer += ","
        answer += "]"
    print(answer)