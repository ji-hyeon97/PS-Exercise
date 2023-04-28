import sys

while True:
    data = sys.stdin.readline().rstrip()
    stack = ['']
    check = [1]

    if data == '.':
        break

    for i in data:
        if i == '(':
            stack.append(i)
            continue
        if i == '[':
            stack.append(i)
            continue

        if i == ')' and stack[-1] == '(':
            stack.pop()
            continue
        if i == ')' and stack[-1] != '(':
            check[0] = 0

        if i == ']' and stack[-1] == '[':
            stack.pop()
            continue

        if i == ']' and stack[-1] != '[':
            check[0] = 0

    if len(stack) == 1 and check[0] == 1:
        print('yes')
    else:
        print('no')
