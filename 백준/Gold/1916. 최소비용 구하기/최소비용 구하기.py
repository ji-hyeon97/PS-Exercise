import sys
import heapq

n = int(sys.stdin.readline().rstrip())
dist = [int(1e9) for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

m = int(sys.stdin.readline().rstrip())
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])

start, end = map(int, sys.stdin.readline().split())
dist[start] = 0
data = []

heapq.heappush(data, [0, start])
while data:
    cost, node = heapq.heappop(data)
    if cost > dist[node]: 
        continue
    for a, b in graph[node]:
        if dist[b] > dist[node] + a:
            dist[b] = dist[node] + a
            heapq.heappush(data, [dist[b], b])

print(dist[end])