import sys
import heapq

n, e = map(int, sys.stdin.readline().split())
data = []
dist = [int(1e9) for _ in range(n + 1)]
dist[1] = 0
graph = [[] for _ in range(n + 1)]

heapq.heappush(data, [0, 1])

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

v1, v2 = map(int, sys.stdin.readline().split())

while data:
    cost, node = heapq.heappop(data)
    if cost > dist[node]:
        continue
    for a, b in graph[node]:
        if dist[b] > dist[node] + a:
            dist[b] = dist[node] + a
            heapq.heappush(data, [dist[b], b])

dist1 = [int(1e9) for _ in range(n + 1)]
dist1[n] = 0
heapq.heappush(data, [0, n])

while data:
    cost, node = heapq.heappop(data)
    if cost > dist1[node]:
        continue
    for a, b in graph[node]:
        if dist1[b] > dist1[node] + a:
            dist1[b] = dist1[node] + a
            heapq.heappush(data, [dist1[b], b])

dist2 = [int(1e9) for _ in range(n + 1)]
dist2[v1] = 0
heapq.heappush(data, [0, v1])

while data:
    cost, node = heapq.heappop(data)
    if cost > dist2[node]:
        continue
    for a, b in graph[node]:
        if dist2[b] > dist2[node] + a:
            dist2[b] = dist2[node] + a
            heapq.heappush(data, [dist2[b], b])

middle = dist2[v2]
answer = min(dist[v1] + dist1[v2] + middle, dist[v2] + dist1[v1] + middle)

if answer >= int(1e9):
    print(-1)
else:
    print(answer)