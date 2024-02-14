import sys

n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
    data = list(map(str, sys.stdin.readline().rstrip()))
    graph.append(data)


def sol(x, y, n):
    target = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != target:
                target = -1
                break
    if target == -1:
        n = n // 2
        print("(", end="")
        sol(x, y, n)
        sol(x, y + n, n)
        sol(x + n, y, n)
        sol(x + n, y + n, n)
        print(")", end="")

    if target == '1':
        print(1, end="")
    if target == '0':
        print(0, end="")


sol(0, 0, n)