import sys

n = int(sys.stdin.readline().rstrip())

graph = []
for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)

city = [[] for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            city[i].append(j)

answer = int(1e9)
dist = 0
for i in range(n):
    def dfs(node, original):
        global answer
        global dist

        temp = 0
        for k in check:
            if k == 1:
                temp += 1
        if temp == n:
            if graph[node][original] != 0:
                answer = min(answer, dist + graph[node][original])
            return
        for k in city[node]:
            if check[k] == 0:
                check[k] = 1
                dist += graph[node][k]
                dfs(k, original)
                check[k] = 0
                dist -= graph[node][k]


    check = [0 for _ in range(n + 1)]
    check[i] = 1
    dfs(i, i)

print(answer)