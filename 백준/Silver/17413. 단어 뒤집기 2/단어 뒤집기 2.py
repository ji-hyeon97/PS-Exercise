import sys
from collections import deque

data = list(map(str, sys.stdin.readline().rstrip()))
stack = []
test = deque()
flag = 0

for i in data:
    if i == "<":
        while test:
            stack.append(test.pop())
        flag = 1
        stack.append(i)
        continue
    if i == ">":
        flag = 0
        stack.append(i)
        continue

    if flag == 0:
        if i == " ":
            while test:
                stack.append(test.pop())
            stack.append(i)
        else:
            test.append(i)

    if flag == 1:
        stack.append(i)

if test:
    while test:
        stack.append(test.pop())

print("".join(stack))