import sys

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


def dfs(x, cost, target):
    for next, costs in graph[x]:
        if next == target:
            print(cost + costs)
            return
        if check[next] == 0:
            check[next] = 1
            dfs(next, cost + costs, target)


for _ in range(M):
    source, target = map(int, sys.stdin.readline().split())
    check = [0 for _ in range(N + 1)]
    check[source] = 1

    for next, cost in graph[source]:
        if next == target:
            print(cost)
            break
        check[next] = 1
        dfs(next, cost, target)