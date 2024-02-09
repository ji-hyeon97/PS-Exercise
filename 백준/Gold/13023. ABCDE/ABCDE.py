import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

relation = 0


def dfs(node, depth):
    global relation
    check[node] = 1
    relation = max(relation, depth)
    if relation >= 4:
        return
    for i in graph[node]:
        if check[i] == 0:
            dfs(i, depth + 1)
    check[node] = 0


for i in range(n):
    check = [0 for _ in range(n)]
    dfs(i, 0)
    if relation >= 4:
        break

if relation >= 4:
    print(1)
else:
    print(0)