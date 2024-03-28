import sys

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))

check = [[0 for _ in range(m)] for _ in range(n)]

answer = 0


def dfs(x, y):
    global answer
    check[x][y] = 1
    cycle.append([x, y])
    if graph[x][y] == 'D' and x < n - 1:
        x += 1
    if graph[x][y] == 'R' and y < m - 1:
        y += 1
    if graph[x][y] == 'L' and y > 0:
        y -= 1
    if graph[x][y] == 'U' and x > 0:
        x -= 1

    if check[x][y] == 1:
        if [x, y] in cycle:
            answer += 1
            return
    else:
        dfs(x, y)


for i in range(n):
    for j in range(m):
        if check[i][j] == 0:
            cycle = []
            dfs(i, j)

print(answer)