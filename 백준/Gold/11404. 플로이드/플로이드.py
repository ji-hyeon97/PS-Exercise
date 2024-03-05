import sys
import heapq

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])


def shortPath():
    while data:
        cost, node = heapq.heappop(data)
        if cost > dist[node]:
            continue
        for a1, b1 in graph[node]:
            if dist[b1] > a1 + dist[node]:
                dist[b1] = dist[node] + a1
                heapq.heappush(data, [dist[b1], b1])


for i in range(1,n+1):
    data = []
    dist = [int(1e9) for _ in range(n + 1)]
    dist[i] = 0
    heapq.heappush(data, [0, i])
    shortPath()
    for j in range(1,n+1):
        if i == j:
            print(0, end=" ")
        else:
            if dist[j] == int(1e9):
                print(0, end=" ")
            else:
                print(dist[j], end=" ")
    print()