import sys
import heapq

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 3)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

check = [0 for _ in range(n + 3)]
data = [[0, 1]]
answer = 0
count = 0

while data:
    if count == n:
        break
    dist, node = heapq.heappop(data)
    if check[node] == 1:
        continue
    check[node] = 1
    answer += dist
    count += 1
    for a, b in graph[node]:
        heapq.heappush(data, [a, b])

print(answer)