import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n + 5)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

check = [0 for _ in range(n + 1)]


def recur(node, prev):
    check[node] = prev
    for nxt in graph[node]:
        if prev == nxt:
            continue
        recur(nxt, node)


recur(1, 0)
check = check[2:]
for i in check:
    print(i)