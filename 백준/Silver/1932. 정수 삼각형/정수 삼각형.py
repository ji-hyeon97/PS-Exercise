import sys

n = int(sys.stdin.readline().rstrip())
graph = []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)
    if i == 1:
        graph[i][0] += graph[0][0]
        graph[i][1] += graph[0][0]

    if i > 1:
        for j in range(0, i + 1):
            if j == 0:
                graph[i][j] += graph[i - 1][0]
                continue
            if j == i:
                graph[i][j] += graph[i - 1][i - 1]
                continue
            graph[i][j] = max(graph[i][j] + graph[i - 1][j - 1], graph[i][j] + graph[i - 1][j])
print(max(graph[-1]))