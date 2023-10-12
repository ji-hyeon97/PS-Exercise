import sys

n, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
answer = 0

check = [0] * n


def dfs(idx, live):
    global answer
    if live < 0:
        return
    if idx == n:
        answer += 1
        return
    for i in range(n):
        if check[i] == 0:
            check[i] = 1
            dfs(idx + 1, live + data[i] - k)
            check[i] = 0


dfs(0, 0)
print(answer)