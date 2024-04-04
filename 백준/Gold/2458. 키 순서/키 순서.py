import sys

N, M = map(int, sys.stdin.readline().split())
graph1 = [[] for _ in range(N + 1)]
graph2 = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph1[a].append(b)
    graph2[b].append(a)


def dfs1(node):
    for i in graph1[node]:
        if check[i] == 0:
            check[i] = 1
            dfs1(i)


def dfs2(node):
    for i in graph2[node]:
        if check[i] == 0:
            check[i] = 1
            dfs2(i)


answer = 0
for i in range(1, N + 1):
    check = [0 for _ in range(N + 1)]
    check[i] = 1
    dfs1(i)
    dfs2(i)

    if N == sum(check):
        answer += 1
print(answer)