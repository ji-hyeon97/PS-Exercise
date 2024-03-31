import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

ddx = [-1, -1, 1, 1]
ddy = [-1, 1, -1, 1]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    cloud2 = []
    check = [[0 for _ in range(n)] for _ in range(n)]
    for x, y in cloud:
        nx = (x + dx[a] * b) % n
        ny = (y + dy[a] * b) % n
        graph[nx][ny] += 1
        check[nx][ny] = 1
        cloud2.append((nx, ny))

    for x, y in cloud2:
        temp = 0
        for i in range(4):
            nx = x + ddx[i]
            ny = y + ddy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] > 0:
                temp += 1
        graph[x][y] += temp

    cloud = []
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0 and graph[i][j] >= 2:
                graph[i][j] -= 2
                cloud.append((i, j))

answer = 0
for data in graph:
    answer += sum(data)
print(answer)