import sys
import heapq

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n + 1)]
dist = [int(1e9) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])

start, end = map(int, sys.stdin.readline().split())
dist[start] = 0
data = []
heapq.heappush(data, [0, start])
prev_node = [0] * (n + 1)

while data:
    cost, node = heapq.heappop(data)
    if cost > dist[node]:
        continue
    for a, b in graph[node]:
        if dist[b] > dist[node] + a:
            dist[b] = dist[node] + a
            prev_node[b] = node
            heapq.heappush(data, [dist[b], b])

print(dist[end])
path = [end]
now = end
while now != start:
    now = prev_node[now]
    path.append(now)
path.reverse()
print(len(path))
for i in path:
    print(i, end=" ")