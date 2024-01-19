import sys

data = list(map(str,sys.stdin.readline().rstrip()))
target = sys.stdin.readline().rstrip()
stack = []
l = len(target)

for i in data:
    stack.append(i)
    temp = ""
    for i in stack[-l:]:
        temp+=i
    if temp == target:
        for _ in range(l):
            stack.pop()
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))