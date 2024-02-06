import sys

n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)

check = [0 for _ in range(n + 1)]


def dfs(index):
    for i in range(n):
        if check[i] == 0 and graph[index][i] == 1:
            check[i] = 1
            dfs(i)


for i in range(n):
    dfs(i)
    for j in range(n):
        if check[j] == 1:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
    check = [0 for _ in range(n + 1)]