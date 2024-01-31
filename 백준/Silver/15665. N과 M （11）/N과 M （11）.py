import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
stack = []
dic = {}


def backtracking():
    if len(stack) == m and tuple(stack) not in dic:
        dic[tuple(stack)] = 1
        for i in stack:
            print(i, end=" ")
        print()
        return

    for i in data:
        stack.append(i)
        if tuple(stack) not in dic:
            backtracking()
        stack.pop()


backtracking()