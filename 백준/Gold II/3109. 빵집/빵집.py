import sys

r, c = map(int, sys.stdin.readline().split())
graph = []

for _ in range(r):
    data = list(map(str, sys.stdin.readline().rstrip()))
    graph.append(data)

check = [[0 for _ in range(c + 1)] for _ in range(r + 1)]

answer = 0


def dfs(x, y):
    if y == c - 1:
        return 1
    for dx in [-1, 0, 1]:
        nx = x + dx
        ny = y + 1
        if nx < 0 or nx >= r or ny >= c:
            continue
        if graph[nx][ny] == '.' and check[nx][ny] == 0:
            check[nx][ny] = 1
            if dfs(nx, ny) == 1:
                return 1
    return 0


for i in range(r):
    if dfs(i, 0) == 1:
        answer += 1
print(answer)