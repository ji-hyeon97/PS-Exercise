import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

stack = [0]
dic = {}


def backtracking():
    if len(stack) == m + 1 and tuple(stack) not in dic:
        dic[tuple(stack)] = 1
        for i in stack:
            if i == 0:
                continue
            print(i, end=" ")
        print()
        return
    for i in data:
        if tuple(stack) not in dic and i >= stack[-1]:
            stack.append(i)
            backtracking()
            stack.pop()


backtracking()