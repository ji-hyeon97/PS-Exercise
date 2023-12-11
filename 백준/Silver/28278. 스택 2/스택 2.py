import sys

n = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(n):
    command = list(map(int,sys.stdin.readline().split()))
    if command[0] == 1:
        stack.append(command[1])
    if command[0] == 2:
        if len(stack) == 0:
            print(-1)
            continue
        value = stack.pop()
        print(value)
    if command[0] == 3:
        print(len(stack))
    if command[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if command[0] == 5:
        if len(stack) == 0:
            print(-1)
            continue
        print(stack[-1])