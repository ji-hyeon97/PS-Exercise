import sys
import heapq

n, m, r = map(int, sys.stdin.readline().split())
info = [0] + list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n + 2)]
answer = 0
for _ in range(r):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

for i in range(n):
    dist = [int(1e9) for _ in range(n + 1)]
    dist[i] = 0
    data = [[0, i]]

    while data:
        cost, node = heapq.heappop(data)
        if cost > dist[node]:
            continue
        for a, b in graph[node]:
            if dist[b] > cost + a:
                dist[b] = cost + a
                heapq.heappush(data, [dist[b], b])
    temp = 0
    for j in range(len(dist)):
        if dist[j] <= m:
            temp += info[j]

    answer = max(answer, temp)
print(answer)