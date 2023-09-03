import sys

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        if i > 0 and j == 0:
            graph[i][j] = graph[i - 1][j] + graph[i][j]
        if i == 0 and j > 0:
            graph[i][j] = graph[i][j - 1] + graph[i][j]
        if i > 0 and j > 0:
            graph[i][j] = graph[i - 1][j] + graph[i][j - 1] - graph[i - 1][j - 1] + graph[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    answer = 0
    if x1 > 0 and y1 > 0:
        answer = graph[x2][y2] - graph[x2][y1 - 1] - graph[x1 - 1][y2] + graph[x1 - 1][y1 - 1]
    if x1 > 0 and y1 == 0:
        answer = graph[x2][y2] - graph[x1 - 1][y2]
    if x1 == 0 and y1 > 0:
        answer = graph[x2][y2] - graph[x2][y1 - 1]
    if x1 == 0 and y1 == 0:
        answer = graph[x2][y2]
    print(answer)