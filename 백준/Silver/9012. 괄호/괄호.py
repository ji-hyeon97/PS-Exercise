import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    data = sys.stdin.readline().rstrip()
    stack = []
    check = [1]
    for i in data:
        if i == '(':
            stack.append(i)
        if i == ')':
            if len(stack) == 0:
                check[0] = 0
            else:
                if stack[-1] != '(':
                    check[0] = 0
                else:
                    stack.pop()
    if check[0] == 1 and len(stack) == 0:
        print("YES")
    else:
        print("NO")