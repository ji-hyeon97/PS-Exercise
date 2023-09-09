import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])

dist = [1e9 for _ in range(v + 1)]
dist[start] = 0
queue = []
heapq.heappush(queue, [0, start])

while queue:
    w, node = heapq.heappop(queue)
    for a, b in graph[node]:
        if dist[a] > dist[node] + b:
            dist[a] = dist[node] + b
            heapq.heappush(queue, [dist[a], a])

for i in range(1, len(dist)):
    if dist[i] == 1e9:
        print("INF")
    else:
        print(dist[i])