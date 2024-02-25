import sys
import heapq

n, m, x = map(int, sys.stdin.readline().split())
toFrom = [int(1e9) for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
toFrom[x] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])

data = []
heapq.heappush(data, [0, x])

while data:
    cost, node = heapq.heappop(data)
    if cost > toFrom[node]:
        continue
    for a, b in graph[node]:
        if toFrom[b] > toFrom[node] + a:
            toFrom[b] = toFrom[node] + a
            heapq.heappush(data, [toFrom[b], b])

answer = 0


def minPath(start):
    global fromTo
    fromTo[start] = 0
    heapq.heappush(data, [0, start])
    while data:
        cost, node = heapq.heappop(data)
        if cost > fromTo[node]:
            continue
        for a, b in graph[node]:
            if fromTo[b] > fromTo[node] + a:
                fromTo[b] = fromTo[node] + a
                heapq.heappush(data, [fromTo[b], b])


for i in range(1, n + 1):
    fromTo = [int(1e9) for _ in range(n + 1)]
    minPath(i)
    answer = max(answer, fromTo[x] + toFrom[i])
print(answer)