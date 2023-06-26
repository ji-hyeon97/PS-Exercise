import sys

data = list(map(str, sys.stdin.readline().rstrip()))
stack = []
answer = 0

for i in range(len(data)):
    if data[i] == '(':
        stack.append(i)
    else:
        stack.pop()
        if data[i - 1] == "(":
            answer += len(stack)
        else:
            answer += 1
print(answer)