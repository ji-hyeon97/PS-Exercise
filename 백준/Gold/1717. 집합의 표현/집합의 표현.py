import sys

sys.setrecursionlimit(10 ** 6)


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    x, a, b = map(int, sys.stdin.readline().split())

    if x == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")