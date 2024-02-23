import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

q = [[0, 1]]
answer = 0
cnt = 0

while q:
    if cnt == n:
        break
    weight, node = heapq.heappop(q)

    if visit[node] == 0:
        visit[node] = 1
        answer += weight
        cnt += 1

        for nxt in graph[node]:
            heapq.heappush(q, nxt)
print(answer)