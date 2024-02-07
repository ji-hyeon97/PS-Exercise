import sys

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i, j))
        if graph[i][j] == 2:
            chicken.append((i, j))

answer = int(1e9)


def cal(list):
    distance = 0
    for a, b in home:
        temp = int(1e9)
        for c, d in list:
            temp = min(temp, abs(a - c) + abs(b - d))
        distance += temp
    return distance


def recur(depth, list):
    global answer
    if depth == len(chicken):
        if len(list) == m:
            answer = min(answer, cal(list))
        return
    recur(depth + 1, list)
    recur(depth + 1, list + [chicken[depth]])


recur(0, [])
print(answer)