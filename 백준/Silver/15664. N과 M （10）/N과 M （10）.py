import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
stack = [0]
check = [0 for _ in range(n)]
dic = {}


def backtracking():
    if len(stack) == m + 1 and tuple(stack) not in dic:
        dic[tuple(stack)] = 1
        for i in stack:
            if i == 0:
                continue
            print(i, end=" ")
        print("")
        return
    for i in range(n):
        if check[i] == 0 and stack[-1] <= data[i]:
            check[i] = 1
            stack.append(data[i])
            backtracking()
            stack.pop()
            check[i] = 0


backtracking()