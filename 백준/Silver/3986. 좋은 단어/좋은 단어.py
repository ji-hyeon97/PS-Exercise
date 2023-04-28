import sys

n = int(sys.stdin.readline().rstrip())

count = 0
for _ in range(n):
    data = sys.stdin.readline().rstrip()
    stack = []
    if len(data) % 2 == 1:
        continue

    for i in data:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    if len(stack)==0:
        count+=1
print(count)
