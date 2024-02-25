import sys
import heapq

n, m, k, x = map(int, sys.stdin.readline().split())
data = []
dist = [int(1e9) for _ in range(n + 1)]
dist[x] = 0
heapq.heappush(data, [0, x])

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append([1, b])

while data:
    cost, node = heapq.heappop(data)
    for a, b in graph[node]:
        if dist[b] > dist[node] + a:
            dist[b] = dist[node] + a
            heapq.heappush(data, [dist[b], b])

flag = 0
for i in range(1, n + 1):
    if dist[i] == k:
        flag = 1
        print(i)
if flag == 0:
    print(-1)