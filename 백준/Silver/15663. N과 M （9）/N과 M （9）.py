import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
check = [0 for _ in range(n)]
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
    for i in range(n):
        if check[i] == 0:
            check[i] = 1
            stack.append(data[i])
            backtracking()
            stack.pop()
            check[i] = 0


backtracking()