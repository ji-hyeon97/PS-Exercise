import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 2)]
dist = [int(1e9) for _ in range(N + 2)]
data = []

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

dist[1] = 0
heapq.heappush(data, [0, 1])

while data:
    cost, node = heapq.heappop(data)
    for a,b in graph[node]:
        if dist[a] > cost + b:
            dist[a] = cost + b
            heapq.heappush(data, [dist[a], a])

print(dist[N])