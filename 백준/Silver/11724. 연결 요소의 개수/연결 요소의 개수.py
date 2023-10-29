import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

check = [0 for _ in range(n + 1)]


def dfs(index):
    for i in graph[index]:
        if check[i] == 0:
            check[i] = 1
            dfs(i)


answer = 0
for i in range(1, n + 1):
    if check[i] == 0:
        check[i] = 1
        dfs(i)
        answer += 1

print(answer)